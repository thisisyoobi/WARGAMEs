#!/usr/bin/env python3

'''
# Summary
- read user dir's flag file
'''


from pwn import *

#context.log_level = 'debug'

s = ssh(host='ctf.redraccoon.kr', port=31338, user='rcity0', password='rcity0')
flag = s['cat flag']
print(b"flag : "+flag)
s.close()