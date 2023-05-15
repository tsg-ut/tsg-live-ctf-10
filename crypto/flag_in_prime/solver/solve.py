# coding: utf-8
from output import N,e,c,d
flag_len = 64
tmp=(e*d-1)
tmp = tmp//(tmp//N+1)
pplusq = -tmp+N+1
from math import isqrt
isqrt(pplusq**2-4*N)
pminusq=isqrt(pplusq**2-4*N)
p = (pplusq+pminusq)//2
assert(N%p==0)
q = N//p
print(p.to_bytes(flag_len,'little'))
print(q.to_bytes(flag_len,'little'))
