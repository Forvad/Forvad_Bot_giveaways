import asyncio
import time
import requests
from sys import stderr
from aiohttp import ClientSession, ClientResponseError
from pyuseragents import random as random_useragent
from loguru import logger
from setup import Update
from urllib3 import disable_warnings
from os import name
from json import loads

re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
disable_warnings()
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> - <level>{message}</level>")


def headers(r, auth):
    headers = {'authorization': token_set[r],
               'user-agent': str(random_useragent()),
               'sec-ch-ua-platform': 'Windows',
               'accept-language': 'ru-BY,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
               'accept-encoding': 'gzip, deflate, br',
               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
               'x-debug-options': 'bugReporterEnabled',
               'discord-locale': 'ru'
               }
    if auth in 'p':
        return headers
    else:
        return headers['authorization']



async def fetch_url_data(session, url, r):
    if emoji_bot in '1':
        try:
            if proxy in 'yes':
                async with session.put(url, timeout=60, headers=headers(r, 'p'), proxy={
                    'http': f'http://{proxy_set[r]}',
                    'https': f'http://{proxy_set[r]}'}) \
                        as response:
                    resp = await response.read()
            else:
                async with session.put(url, timeout=60, headers=headers(r, 'p')) as response:
                    resp = await response.read()
            return logger.success(f'**Emotion delivered** {headers(r,"e")}')
        except Exception as e:
            print(e)
    else:
        try:
            if proxy in 'yes':
                async with session.put(url, timeout=60, headers=headers(r, 'p'), json=payload, proxy={
                    'http': f'{proxy_set[r]}',
                    'https': f'{proxy_set[r]}'}) \
                        as response:
                    resp = await response.read()
            else:
                async with session.put(url, timeout=60, json=payload, headers=headers(r, 'p')) as response:
                    resp = await response.read()
            return logger.success(f'**Emotion delivered** {headers(r,"e")}')
        except Exception as e:
            print(e)


async def fetch_async(loop, number):
    if number in '1':
        url = f'https://discord.com/api/v9/channels/{data[0]}/messages/{data[1]}/reactions/{data[2]}/@me?location=Message'
    else:
        url = 'https://discord.com/api/v9/interactions'
    tasks = []
    async with ClientSession() as session:
        for i in range(len(token_set)):
            task = asyncio.ensure_future(fetch_url_data(session, url, i))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


def token_verification(auth):
    global online
    session = requests.Session()
    session.headers.update(headers(auth, 'p'))
    r = session.get(
        f'https://discord.com/api/v9/channels/{chanel_id}/messages?limit=50')
    if r.status_code == 200 and len(loads(r.text)) > 0:
        online += 1
        return logger.success(f'Token Valid {headers(auth, "e")}')
    else:
        return logger.error(f'Token False {headers(auth, "e")} ')


Access = True
Setup = Update()
if 'posix' in name:
    pass
else:
    Setup.banner()
emoji_bot = input(f'{gr}emoji - 1{cy} / {re}bot giveaways - 2{cy} / TEST token - 3\n Enter the:')
if emoji_bot in '1':
    data = input(f"{cy}do I need to change the config? {gr}ChanelId{cy}/{re}MessageID{cy}/Emoji\n Enter the: ") \
        .split('/')
elif emoji_bot in '2':
    payload = open('paloyd.txt', 'r', encoding='utf-8').read()
    if len(payload) < 1:
        logger.error('Enter the text in payload.txt')
        Access = False
elif emoji_bot in '3':
    chanel_id = input('chanel id: ')
    token_set: list = open('token.txt', 'r', encoding='latin-1').read().splitlines()
    online = 0
    for i in range(len(token_set)):
        token_verification(i)
        Access = False
    print(f'{gr}Online tokens: {cy}{online}{gr} from {re}{len(token_set)}{gr}')
else:
    logger.error('Enter 1, 2 or 3')
    Access = False


if Access:
    token_set: list = open('token.txt', 'r', encoding='latin-1').read().splitlines()
    proxy = input(f'need proxy? {gr}yes{cy} / {re}no{cy}\n Enter the: ').lower()
    print('proxy http://login:pass@id:port --->> proxy.txt')
    if proxy in 'yes':
        proxy_set: list = open('proxy.txt', 'r', encoding='latin-1').read().splitlines()
        if len(token_set) > len(proxy_set):
            confirmation = input(f'Do you have more tokens than a proxy,'
                                 f' do you want to continue without a proxy? '
                                 f'{gr}yes{cy} / {re}no{cy}\n Enter the: ').lower()
            if confirmation in 'no':
                Access = False
            else:
                proxy = 'no'

if __name__ == '__main__' and Access:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_async(loop, emoji_bot))
