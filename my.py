import requests
import json

search = "현대 자동차"

headers = {'Content-Type': 'application/json; charset=utf-8'}
# URL = 'https://openapi.naver.com/v1/search/news.json?query=' + search + '&display=3&start=3&sort=sim'
i = 0
# temp = (1 + i * 100)
URL = 'https://openapi.gg.go.kr/TfcacdarM?KEY=544890ac96d74bf3a044e5c01698e102&Type=json&pSize=253'
res = requests.get(URL, headers=headers, verify=False)
var = json.loads(res.text)
print(URL)
with open('data.json', 'w', encoding="utf-8") as outfile:
    json.dump(var, outfile, ensure_ascii=False)
# for i in range(10):
#     temp = (1 + i * 100)
#     URL = 'https://openapi.naver.com/v1/search/news.json?query=' + search + '&display=100&start=' + str(
#         temp) + '&sort=sim'
#     res = requests.get(URL, headers=headers)
#     var = json.loads(res.text)
#     print(URL)
#     with open('data' + str(i) + '.json', 'w', encoding="utf-8") as outfile:
#         json.dump(var, outfile, ensure_ascii=False)
