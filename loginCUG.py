import requests
import re

url = "http://192.168.168.46/?$USERURL"
data = {
    'username': '20161002214',
    'password': '18279527706'
}
r = requests.post(url=url, data=data)
html = r.text
result = re.findall(r"addInput\('0','0','172.29.218.90','(.+?)','http://192.168.168.46:9999'", html)
# edu or connect
firstNum = result[0]
baseUrl = "http://192.168.168.46:9999/?POSTLanmanUserURL&Lanmannumber="
nextUrl = baseUrl + firstNum
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'userViewURL_cookie=%24USERURL',
    'Host': '192.168.168.46:9999',
    'Origin': 'http://192.168.168.46:9999',
    'Referer': 'http://192.168.168.46:9999/?LanmanUserURL=$USERURL',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
r = requests.post(url=nextUrl, headers=headers)
print(r.text)

