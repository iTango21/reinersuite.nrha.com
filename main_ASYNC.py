import requests
import json
import time
from datetime import datetime
from calendar import monthrange

import os

import asyncio
import aiohttp

from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox


start_time = ''
tok_ = ''

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
        # asyncio.run(pars_('November', 2021))
        main(m_, y_)
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


async def pars_(month, year):

    global dateStart, dateEnd, start_time, tok_

    mmm = month_arr[f'{month}']

    current_year = datetime.now().year
    days = monthrange(current_year, mmm)[1]

    dateStart = f'{year}-{mmm:02}-01'
    dateEnd = f'{year}-{mmm:02}-{days}'
    print(f'dateStart: {dateStart}')
    print(f'dateEnd: {dateEnd}')

    dir_name_1 = f'{year}_ASYNC/{mmm:02}_{month}'

    start_time = time.time()

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


    async with aiohttp.ClientSession() as session:

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

            print(f'\n{id_} {name_}')

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



            tasks = []

            for x in ccc1:
                id__ = x['classId']
                name__ = x['display']

                # print(f'\t{id__} ---> {name__}')

                task = asyncio.create_task(get_page_data(session, dir_name_2, id_, id__, name__))
                tasks.append(task)
                # print(f'Task: {task}')

            await asyncio.gather(*tasks)

            # print(f'\n===================================================================================\n')


async def get_page_data(session, dir_name_2, id_, id__, name__):

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

    link_ = f'https://data.nrha.com/api/app/rs/events/class-sets/classes/approved/{id__}/results-no-dq'

    async with session.get(url=link_, headers=headers) as response:


        response_text = await response.text()

        xxx = json.loads(response_text)

        items__ = []

        for i in xxx:

            items__.append(
                {
                    "PLACING": i['officialPosition'],
                    "BACK#": i['backNumber'],
                    "HORSE": i['horseName'],
                    "RIDER": i['riderName'],
                    "OWNER": i['ownerName'],
                    "SCORE": i['totalScore'],
                    "GREEN": i['greenPoints'],
                    "YOUTH": i['point'],
                    "EARNINGS(USD)": i['earnings']
                }
            )

            #
            # bool_green = False
            # bool_youth = False
            #
            # try:
            #     green_ = i['greenPoints']
            #     bool_green = True
            # except:
            #     try:
            #         youth_ = i['point']
            #         bool_youth = True
            #     except:
            #         pass
            #
            # if bool_green == True:
            #     items__.append(
            #         {
            #             "PLACING": i['officialPosition'],
            #             "BACK#": i['backNumber'],
            #             "HORSE": i['horseName'],
            #             "RIDER": i['riderName'],
            #             "OWNER": i['ownerName'],
            #             "SCORE": i['totalScore'],
            #             "GREEN": green_,
            #             "EARNINGS(USD)": i['earnings']
            #         }
            #     )
            # elif bool_youth == True:
            #     items__.append(
            #         {
            #             "PLACING": i['officialPosition'],
            #             "BACK#": i['backNumber'],
            #             "HORSE": i['horseName'],
            #             "RIDER": i['riderName'],
            #             "OWNER": i['ownerName'],
            #             "SCORE": i['totalScore'],
            #             "YOUTH": youth_,
            #             "EARNINGS(USD)": i['earnings']
            #         }
            #     )
            # else:
            #     items__.append(
            #         {
            #             "PLACING": i['officialPosition'],
            #             "BACK#": i['backNumber'],
            #             "HORSE": i['horseName'],
            #             "RIDER": i['riderName'],
            #             "OWNER": i['ownerName'],
            #             "SCORE": i['totalScore'],
            #             "NONE": 'NONE',
            #             "EARNINGS(USD)": i['earnings']
            #         }
            #     )

        file_name__ = f'{name__}' \
            .replace("?", "") \
            .replace("#", "") \
            .replace(" ", "") \
            .replace("\\", "") \
            .replace("/", "") \
            .replace('"', '=') \
            .replace("*", "")

        fff = f'{dir_name_2}/{id_}_{id__}_{file_name__}.json'
        # print(f'\tWrite: {file_name__}')
        print(f'\t{id__} ---> {name__}')

        with open(fff, 'w', encoding='utf-8') as file:
            json.dump(items__, file, indent=4, ensure_ascii=False)


def main(m, y):
    global start_time

    asyncio.run(pars_(m, y))
    finish_time = time.time() - start_time
    print(f'\nTIME: {finish_time}')


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    window.run()
