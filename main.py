import requests
import json
import time
from datetime import datetime


start_time = time.time()

with open('config.json', 'r', encoding='utf-8') as set_:
    set_data = json.load(set_)

year_from = set_data['year_from']
year_to = set_data['year_to']

set_email = set_data['set_email']
set_pass = set_data['set_pass']

data = '{"username":"adgoldtx@gmail.com","password":"W@y!@ndDr1"}'

headers = {
    'authority': 'data.nrha.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'content-type': 'text/plain',
    'origin': 'https://reinersuite.nrha.com',
    'referer': 'https://reinersuite.nrha.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


with requests.Session() as session:

    response = requests.post('https://data.nrha.com/api/app/rs/auth/login', headers=headers, data=data)

    # print(response.json())
    #
    tok__ = json.loads(response.text)
    tok_ = tok__['access']
    print(tok_)

    url_new = 'https://reinersuite.nrha.com/#/app/events/my-events'

    headers = {
        'authority': 'data.nrha.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'authorization': f'Bearer {tok_}',
        'content-type': 'application/json',
        'origin': 'https://reinersuite.nrha.com',
        'referer': 'https://reinersuite.nrha.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    json_data = {
        'affiliateName': '',
        'name': None,
        'countryId': '',
        'stateId': '',
        'affiliateId': None,
        'eventId': None,
        'showId': None,
        'memberId': None,
        'partialNameMatching': True,
        'partialMatch': True,
        'onlyMyEvents': False,
        'topTen': False,
        'startDate': '2021-11-25T00:00:00.000Z',
        'endDate': '2021-12-04T00:00:00.000Z',
    }

    response = requests.post('https://data.nrha.com/api/app/rs/events/search/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{\n  "affiliateName": "",\n  "name": null,\n  "countryId": "",\n  "stateId": "",\n  "affiliateId": null,\n  "eventId": null,\n  "showId": null,\n  "memberId": null,\n  "partialNameMatching": true,\n  "partialMatch": true,\n  "onlyMyEvents": false,\n  "topTen": false,\n  "startDate": "2021-11-25T00:00:00.000Z",\n  "endDate": "2021-12-04T00:00:00.000Z"\n}'
    # response = requests.post('https://data.nrha.com/api/app/rs/events/search/', headers=headers, data=data)

    aaa1 = json.loads(response.text)

    with open(f'aaa1.json', 'w', encoding='utf-8') as file:
        json.dump(aaa1, file, indent=4, ensure_ascii=False)

    headers = {
        'authority': 'data.nrha.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'authorization': f'Bearer {tok_}',
        'content-type': 'text/plain',
        'origin': 'https://reinersuite.nrha.com',
        'referer': 'https://reinersuite.nrha.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://data.nrha.com/api/app/rs/events/72406', headers=headers)

    bbb1 = json.loads(response.text)

    headers = {
        'authority': 'data.nrha.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'authorization': f'Bearer {tok_}',
        'content-type': 'text/plain',
        'origin': 'https://reinersuite.nrha.com',
        'referer': 'https://reinersuite.nrha.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://data.nrha.com/api/app/rs/events/72406/calculate-level', headers=headers)

    bbb2 = json.loads(response.text)

    with open(f'bbb1.json', 'w', encoding='utf-8') as file:
        json.dump(bbb1, file, indent=4, ensure_ascii=False)

    with open(f'bbb2.json', 'w', encoding='utf-8') as file:
        json.dump(bbb2, file, indent=4, ensure_ascii=False)

    headers = {
        'authority': 'data.nrha.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'authorization': f'Bearer {tok_}',
        'content-type': 'text/plain',
        'origin': 'https://reinersuite.nrha.com',
        'referer': 'https://reinersuite.nrha.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://data.nrha.com/api/app/rs/events/72406/results', headers=headers)

    ccc1 = json.loads(response.text)

    headers = {
        'authority': 'data.nrha.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'authorization': f'Bearer {tok_}',
        'content-type': 'text/plain',
        'origin': 'https://reinersuite.nrha.com',
        'referer': 'https://reinersuite.nrha.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://data.nrha.com/api/app/rs/events/72406/calculate-level', headers=headers)

    ccc2 = json.loads(response.text)

    with open(f'ccc1.json', 'w', encoding='utf-8') as file:
        json.dump(ccc1, file, indent=4, ensure_ascii=False)

    with open(f'ccc2.json', 'w', encoding='utf-8') as file:
        json.dump(ccc2, file, indent=4, ensure_ascii=False)

    headers = {
        'authority': 'data.nrha.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        'authorization': f'Bearer {tok_}',
        'content-type': 'text/plain',
        'origin': 'https://reinersuite.nrha.com',
        'referer': 'https://reinersuite.nrha.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    for x in ccc1:
        id_ = x['classId']

        print(f'ID: {id_}')

        response = requests.get(f'https://data.nrha.com/api/app/rs/events/shows/approved-classes/{id_}', headers=headers)

        ddd = json.loads(response.text)

        with open(f'{id_}.json', 'w', encoding='utf-8') as file:
            json.dump(ddd, file, indent=4, ensure_ascii=False)

finish_time = time.time() - start_time
print(f'\nTIME: {finish_time}')
