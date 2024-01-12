#pwntools library is the CTF framework and exploits development library
#it is one of the powerful tools for creting hacking scripts

from pwn import *

print(cyclic(50))    #create a sequence of 50 bytes
print(cyclic_find("laaa"))      #give the offset of "laaa" in the given 50 bytes sequence

print("-------------")

print(shellcraft.sh())    #gives the assembly or shell code of xxv
print(hexdump(asm(shellcraft.sh())))     #gives the hex dump of the ASM for the shellcraft shellcode

print("-------------")

#setup local process
# p = process("/bin/sh")
# p.sendline("echo hello;")
# p.interactive()
# p.close()

print("-------------")

#remote process
# r = remote("127.0.0.1", 1234)    #listen to the same port using netcat
# r.sendline("hello")
# r.interactive()       #interactive session
# r.close()

print("-------------")

#packing and unpacking numbers for exploits and passing data over the network
print(p32(0x1337))
print(hex(u32(p32(0x1337))))

print("-------------")

#load files
l = ELF("/bin/bash")

print(hex(l.address))   #gives the base address
print(hex(l.entry))     #gives the entry point

print("-------------")

print(hex(l.got['write']))   #know the address for the specific symbol form global offset table
print(hex(l.plt['write']))   #grab information of specific symbol from procedure linkage table

print("-------------")

for address in l.search(b'/bin/sh\x00'):     #search directly in the ELF file for the string "/bin/sh" with null terminator
	print(hex(address))

print("-------------")

print(hex(next(l.search(asm('jmp esp')))))     #search for "jmp esp" gadget

print("-------------")

#alternative search method for gadget using ROP function
r = ROP(l)
print(r.rbx)

print("-------------")

#some encryption, encoding and hashing functions imported by pwntools library
print(xor("A", "B"))              #xoring
print(xor(xor("A", "B"), "A"))    #xoring again to get initial character

print(b64e(b"test"))       #base-64 encoding of test
print(b64d(b"dGVzdA=="))   #base-64 decoding of the given hash
print(md5sumhex(b"hello"))    #md5 encoding
print(sha1sumhex(b"hello"))   #sha-1 encoding

print(bits(b"a"))       #bits representation of 'a'
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))    #unbits representation of 'a'

# for learning on more functionalities of pwntools, visit the official documentation: https://docs.pwntools.com
