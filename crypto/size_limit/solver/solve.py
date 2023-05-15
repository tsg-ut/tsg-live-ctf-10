#!/usr/bin/python3
# coding: utf-8

from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from output import N,e,c,d
flag_prefix = b"TSGLIVE{"
flag_len = 131
m = pow(c,d,N)
long_to_bytes(m)
tmp = flag_prefix+b"\x00"*(flag_len-len(flag_prefix))
tmp = bytes_to_long(tmp)
mm=((tmp-m)//N+1)*N+m
print(long_to_bytes(mm))
