import json
import requests
import execjs

with open('07test.js','r',encoding='utf_8') as f:
    json_code = f.read()
cts=execjs.compile(json_code)
json_data=cts.call('encrypt')

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "m": json_data['m'],
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.mashangpa.com/problem-detail/7/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"153\", \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"153\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "ts": str(json_data['ts']),
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "1tu896stybfwq1e26xamun14m27wv0ub",
    "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0": "1789398531,1789479069,1789484356,1789539070",
    "HMACCOUNT": "D13DF6301D1BC327",
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1789539085"
}
url = 'https://www.mashangpa.com/api/problem-detail/7/data/'
total_num=0
for i in range(1,21):
    params = {
        "page": i,
        "x": json_data['x']
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    json_data1 = cts.call('xxxxoooo',response.json()['r'])
    json_num = json.loads(json_data1)['current_array']
    page_num = sum(json_num)
    total_num += page_num
print(total_num)