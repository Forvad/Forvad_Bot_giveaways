import asyncio
import time
from sys import stderr
from aiohttp import ClientSession, ClientResponseError
from pyuseragents import random as random_useragent
from loguru import logger
from setup import Update
from urllib3 import disable_warnings
from os import  name


re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
disable_warnings()
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> - <level>{message}</level>")

async def fetch_url_data(session, url, r):
    _headers = {'authorization': token_set[r],
                'user-agent': str(random_useragent()),
                'sec-ch-ua-platform': 'Windows',
                'accept-language': 'ru-BY,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
                'accept-encoding': 'gzip, deflate, br',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                'x-debug-options': 'bugReporterEnabled',
                'discord-locale': 'ru'
                }
    try:
        if proxy in 'yes':
            async with session.put(url, timeout=60, headers=_headers, proxy={
                'http': f'http://{proxy_set[r]}',
                'https': f'http://{proxy_set[r]}'})\
                    as response:
                resp = await response.read()
        else:
            async with session.put(url, timeout=60, headers=_headers) as response:
                resp = await response.read()
        return logger.success(f'**Emotion delivered** {_headers["authorization"]}')
    except Exception as e:
        print(e)


async def fetch_async(loop):
    url = f'https://discord.com/api/v9/channels/{data[0]}/messages/{data[1]}/reactions/{data[2]}/@me?location=Message'
    tasks = []
    async with ClientSession() as session:
        for i in range(len(token_set)):
            task = asyncio.ensure_future(fetch_url_data(session, url, i))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses

Setup = Update()
if 'posix' in name:
    pass
else:
    Setup.banner()
token_set: list = open('token.txt', 'r', encoding='latin-1').read().splitlines()
data = input(f"{cy}do I need to change the config? {gr}ChanelId{cy}/{re}MessageID{cy}/Emoji\n Enter the: ")\
    .split('/')
proxy = input(f'need proxy? {gr}yes{cy} / {re}no{cy}\n Enter the: ').lower()
print('proxy http://login:pass@id:port --->> proxy.txt')
Proxy = True
if proxy in 'yes':
    proxy_set: list = open('proxy.txt', 'r', encoding='latin-1').read().splitlines()
    if len(token_set) > len(proxy_set):
        confirmation = input(f'Do you have more tokens than a proxy,'
                             f' do you want to continue without a proxy? '
                             f'{gr}yes{cy} / {re}no{cy}\n Enter the: ').lower()
        if confirmation in 'no':
            Proxy = False
        else:
            proxy = 'no'



if __name__ == '__main__' and Proxy:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_async(loop))
