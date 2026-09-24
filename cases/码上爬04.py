import requests
import execjs
with open("码上爬04.js", "r", encoding="utf-8") as f:
    js_code = f.read()
cts = execjs.compile(js_code)
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.mashangpa.com/problem-detail/4/",
    "sec-ch-ua": '"Chromium";v="152", "Not?A_Brand";v="24", "Microsoft Edge";v="152"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0",
}
cookies = {
    "sessionid": "1tu896stybfwq1e26xamun14m27wv0ub",
    "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0": "1788954938,1789014078",
    "HMACCOUNT": "D13DF6301D1BC327",
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1789014952",
}
url = "https://www.mashangpa.com/api/problem-detail/4/data/"
num = 0
for page in range(1, 21):
    js_data = cts.call("loadPage", page)
    params = {
        "page": page,
        "sign": js_data["sign"],
        "_ts": js_data["_ts"],
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    number = response["current_array"]
    num += sum(number)
print(num)
