import requests

headers = headers = {
    'User-Agent': 'spamtest (spam8155@hotmail.com)',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'data.sec.gov'  # Note the change in the Host to match the subdomain
}

def func(url, lis2):
    res = requests.get(url, headers=headers)
    res = res.json()['facts']['us-gaap']
    empt = []
    for item in res:
        firstval, sec = list(res[item]['units'].items())[0]
        if sec[-1]['fy'] == 2023 or sec[-1]['fy'] == 2024:
            if item in lis2:
                empt.append(item)
    print(empt)
    return empt
urls = ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0001507605.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0000037996.json"
        ,"https://data.sec.gov/api/xbrl/companyfacts/CIK0000012927.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0001585521.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json",
        "https://data.sec.gov/api/xbrl/companyfacts/CIK0000100517.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0001397187.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0001463101.json"]
url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json" ## gets all company facts

result = requests.get(url, headers=headers)



result = result.json()
result = result['facts']
result = result['us-gaap']
lis = []
for item in result:
    firstval, sec = list(result[item]['units'].items())[0]

    if sec[-1]['fy'] == 2023:
        lis.append(item)

for url in urls:
    lis = func(url, lis)

print(lis)
