import requests
import json
import time
from datetime import datetime
from calendar import monthrange

import os

from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox


link_ = ''

month_ = ''
year_ = ''

month_arr = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }

options_month = ('September', 'October', 'November')
options_year = (2021, 2022)

class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        # if icon:
        #     self.root.iconbitmap(icon)

        self.entry = Entry(self.root, width=35, fg='blue', font=("Verdana", 12), relief=SUNKEN, bd=5)

        global options_month
        self.month = Combobox(self.root, values=options_month, state="readonly", width=25)

        global options_year
        self.year = Combobox(self.root, values=options_year, state="readonly", width=25)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        text_var = StringVar(value="Text")
        #Entry(self.root, width=100, fg='blue', font=("Verdana", 12), relief=SUNKEN, bd=5, textvariable=text_var).pack()
        self.entry.pack()
        # Button(self.root, text="Go!..", width=10, command=self.get_link).pack()


        # Button(self.root, text="Get...", width=10, command=self.parse).pack()
        #Combobox(self.root, values=("one", "two", "three"), justify=CENTER).pack()
        self.month.pack()
        self.month.bind("<<ComboboxSelected>>", self.changed)

        self.year.pack()
        self.year.bind("<<ComboboxSelected>>", self.changed)

        Button(self.root, text="Parse!", width=10, command=self.parse).pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def changed(self, event):
        global month_
        index = self.month.get()
        #mb.showinfo("Info", f"Changed value, index: {index}")
        month_ = index
        #-----------------------------------------------------
        global year_
        index = self.year.get()
        #mb.showinfo("Info", f"Changed value, index: {index}")
        year_ = index
        #-----------------------------------------------------

    def get_link(self):
        global link_
        link_ = self.entry.get()
        pg_lnk(link_)

    def parse(self):
        m_ = self.month.get()
        index = self.month.current()
        #mb.showinfo("Get info", f"Index: {index}, value: {value}")
        # -----------------------------------------------------
        y_ = self.year.get()
        index = self.year.current()
        #mb.showinfo("Get info", f"Index: {index}, value: {value}")
        pars_(m_, y_)
        # ------------------------------------------------------

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()



def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def pg_lnk(link_):
    pass


def pars_(month, year):

    global dateStart, dateEnd

    mmm = month_arr[f'{month}']

    current_year = datetime.now().year
    days = monthrange(current_year, mmm)[1]

    dateStart = f'{year}-{mmm:02}-01'
    dateEnd = f'{year}-{mmm:02}-{days}'
    print(f'dateStart: {dateStart}')
    print(f'dateEnd: {dateEnd}')

    dir_name_1 = f'{year}/{mmm:02}_{month}'
    # my_makedirs(dir_name_1)

    start_time = time.time()

    # with open('config.json', 'r', encoding='utf-8') as set_:
    #     set_data = json.load(set_)

    # set_email = set_data['set_email']
    # set_pass = set_data['set_pass']

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
            'startDate': f'{dateStart}T00:00:00.000Z',
            'endDate': f'{dateEnd}T00:00:00.000Z',
        }

        response = requests.post('https://data.nrha.com/api/app/rs/events/search/', headers=headers, json=json_data)

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        # data = '{\n  "affiliateName": "",\n  "name": null,\n  "countryId": "",\n  "stateId": "",\n  "affiliateId": null,\n  "eventId": null,\n  "showId": null,\n  "memberId": null,\n  "partialNameMatching": true,\n  "partialMatch": true,\n  "onlyMyEvents": false,\n  "topTen": false,\n  "startDate": "2021-11-25T00:00:00.000Z",\n  "endDate": "2021-12-04T00:00:00.000Z"\n}'
        # response = requests.post('https://data.nrha.com/api/app/rs/events/search/', headers=headers, data=data)

        aaa = json.loads(response.text)

        for x in aaa:
            id_ = x['id']
            name_ = x['name']

            dir_name_2_ = f'{id_}_{name_}' \
                .replace("#", "") \
                .replace(" ", "_") \
                .replace("\\", "") \
                .replace("/", "") \
                .replace('"', '=') \
                .replace("*", "")

            dir_name_2 = f'./{dir_name_1}/{dir_name_2_}'
            my_makedirs(dir_name_2)

            print(f'{id_} {name_}')

            # headers = {
            #     'authority': 'data.nrha.com',
            #     'accept': 'application/json, text/plain, */*',
            #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
            #     'authorization': f'Bearer {tok_}',
            #     'content-type': 'text/plain',
            #     'origin': 'https://reinersuite.nrha.com',
            #     'referer': 'https://reinersuite.nrha.com/',
            #     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            #     'sec-ch-ua-mobile': '?0',
            #     'sec-ch-ua-platform': '"Windows"',
            #     'sec-fetch-dest': 'empty',
            #     'sec-fetch-mode': 'cors',
            #     'sec-fetch-site': 'same-site',
            #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            # }
            #
            # response = requests.get('https://data.nrha.com/api/app/rs/events/72406', headers=headers)
            #
            # bbb1 = json.loads(response.text)
            #
            # headers = {
            #     'authority': 'data.nrha.com',
            #     'accept': 'application/json, text/plain, */*',
            #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
            #     'authorization': f'Bearer {tok_}',
            #     'content-type': 'text/plain',
            #     'origin': 'https://reinersuite.nrha.com',
            #     'referer': 'https://reinersuite.nrha.com/',
            #     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            #     'sec-ch-ua-mobile': '?0',
            #     'sec-ch-ua-platform': '"Windows"',
            #     'sec-fetch-dest': 'empty',
            #     'sec-fetch-mode': 'cors',
            #     'sec-fetch-site': 'same-site',
            #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            # }
            #
            # response = requests.get('https://data.nrha.com/api/app/rs/events/72406/calculate-level', headers=headers)
            #
            # bbb2 = json.loads(response.text)
            #
            # with open(f'bbb1.json', 'w', encoding='utf-8') as file:
            #     json.dump(bbb1, file, indent=4, ensure_ascii=False)
            #
            # with open(f'bbb2.json', 'w', encoding='utf-8') as file:
            #     json.dump(bbb2, file, indent=4, ensure_ascii=False)

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

            response = requests.get(f'https://data.nrha.com/api/app/rs/events/{id_}/results', headers=headers)

            ccc1 = json.loads(response.text)

            for x in ccc1:
                id__ = x['classId']
                name__ = x['display']

                print(f'\t{id__} ---> {name__}')

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

                response = requests.get(
                    f'https://data.nrha.com/api/app/rs/events/class-sets/classes/approved/{id__}/results-no-dq',
                    headers=headers)

                xxx = json.loads(response.text)

                items__ = []

                for item in xxx:
                    # placing_ = item['officialPosition']
                    # back_ = item['backNumber']
                    # horse_ = item['horseName']
                    # rider_ = item['riderName']
                    # owner_ = item['ownerName']
                    # score_ = item['totalScore']
                    # green_ = item['greenPoints']
                    # youth_ = item['point']
                    # earnings_ = item['earnings']

                    items__.append(
                        {
                            "PLACING": item['officialPosition'],
                            "BACK#": item['backNumber'],
                            "HORSE": item['horseName'],
                            "RIDER": item['riderName'],
                            "OWNER": item['ownerName'],
                            "SCORE": item['totalScore'],
                            "GREEN": item['greenPoints'],
                            "YOUTH": item['point'],
                            "EARNINGS(USD)": item['earnings']
                        }
                    )

                file_name__ = f'{name__}' \
                    .replace("?", "") \
                    .replace("#", "") \
                    .replace(" ", "") \
                    .replace("\\", "") \
                    .replace("/", "") \
                    .replace('"', '=') \
                    .replace("*", "")

                with open(f'{dir_name_2}/{id_}_{id__}_{file_name__}.json', 'w', encoding='utf-8') as file:
                    json.dump(items__, file, indent=4, ensure_ascii=False)


            print(f'\n===================================================================================\n')




        # breakpoint()
        #
        #
        #
        # headers = {
        #     'authority': 'data.nrha.com',
        #     'accept': 'application/json, text/plain, */*',
        #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        #     'authorization': f'Bearer {tok_}',
        #     'content-type': 'text/plain',
        #     'origin': 'https://reinersuite.nrha.com',
        #     'referer': 'https://reinersuite.nrha.com/',
        #     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'same-site',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        # }
        #
        # response = requests.get('https://data.nrha.com/api/app/rs/events/72406/calculate-level', headers=headers)
        #
        # ccc2 = json.loads(response.text)
        #
        # with open(f'ccc1.json', 'w', encoding='utf-8') as file:
        #     json.dump(ccc1, file, indent=4, ensure_ascii=False)
        #
        # with open(f'ccc2.json', 'w', encoding='utf-8') as file:
        #     json.dump(ccc2, file, indent=4, ensure_ascii=False)
        #
        # headers = {
        #     'authority': 'data.nrha.com',
        #     'accept': 'application/json, text/plain, */*',
        #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        #     'authorization': f'Bearer {tok_}',
        #     'content-type': 'text/plain',
        #     'origin': 'https://reinersuite.nrha.com',
        #     'referer': 'https://reinersuite.nrha.com/',
        #     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'same-site',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        # }
        #
        # for x in ccc1:
        #     id_ = x['classId']
        #
        #     print(f'ID: {id_}')
        #
        #     response = requests.get(f'https://data.nrha.com/api/app/rs/events/shows/approved-classes/{id_}', headers=headers)
        #
        #     ddd = json.loads(response.text)
        #
        #     with open(f'{id_}.json', 'w', encoding='utf-8') as file:
        #         json.dump(ddd, file, indent=4, ensure_ascii=False)
        #
        # headers = {
        #     'authority': 'data.nrha.com',
        #     'accept': 'application/json, text/plain, */*',
        #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
        #     'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZGdvbGR0eEBnbWFpbC5jb20iLCJzY29wZXMiOlsiUk9MRV9NRU1CRVIiXSwidXNlciI6MTU5NzIsIm1lbWJlciI6NTA4NDEwLCJvcmciOjEsImlzcyI6Im5yaGEtZGF0YS10amN0cyIsImlhdCI6MTY3MDQ0MTE2NiwiZXhwIjoxNjcwNDQyOTY2fQ.8SlTjuEy6RGeGs7VjQTnts15NXahkjebfVdFG7PO7Koxmy-LB-VamcA-bZJq2GD8EqYAIw3XPUZYX1cQBibfNQ',
        #     'content-type': 'text/plain',
        #     'origin': 'https://reinersuite.nrha.com',
        #     'referer': 'https://reinersuite.nrha.com/',
        #     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'same-site',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        # }
        #
        # response = requests.get(
        #     'https://data.nrha.com/api/app/rs/events/class-sets/classes/approved/5095655/results-no-dq',
        #     headers=headers,
        # )


    finish_time = time.time() - start_time
    print(f'\nTIME: {finish_time}')




if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    window.run()




#     # print(sys.version_info[0])
#     # ЗАПЛАТКА!!! Блок выпадания ОШИБКИ под виндой...
#     if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
#     # asyncio.run(main())
#     main()
