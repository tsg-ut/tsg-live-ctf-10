#!/usr/bin/python3

from Crypto.Util.number import getPrime
from flag import flag
from sympy import nextprime

dummy = b"GSTDIVE{this is a dummy}"

dm = int.from_bytes(dummy,'little')


assert(len(flag)==61)
import secrets

flag = secrets.token_bytes(3) + flag
flag_p = int.from_bytes(flag,'little')

p = nextprime(flag_p)
q = getPrime(512)
N = p * q
phi = (p - 1) * (q - 1)
e = 0x10001
d = pow(e, -1, phi)


c = pow(dm, e, N)

print(f'N = {N}')
print(f'e = {e}')
print(f'c = {c}')
print(f'd = {d}')
