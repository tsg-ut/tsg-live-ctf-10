#!/usr/bin/python3

from Crypto.Util.number import getPrime, bytes_to_long
import flag 
import secrets

assert(len(flag.flag) == 33)

p = getPrime(512)
q = getPrime(512)
N = p * q
phi = (p - 1) * (q - 1)
e = 3
assert(phi%e!=0)
d = pow(e, -1, phi)

m1 = bytes_to_long(flag.flag+secrets.token_bytes(12))
m2 = bytes_to_long(flag.flag+secrets.token_bytes(12))

c1 = pow(m1, e, N)
c2 = pow(m2, e, N)

print(f'N = {N}')
print(f'e = {e}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')
