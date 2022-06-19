from os import system, name
from time import sleep


re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"



class Update:
    def banner(self):

        system("cls")
        print(
                   f'''
                       {re}─╔═╗{cy}─────────────────{re}╔╗{cy}
                       {re}─║╔╝{cy}─────────────────{re}║║{cy}
                       {re}╔╝╚╗{cy}╔══╗{re}╔═╗{cy}╔╗╔╗╔══╗{re}╔═╝║{cy}
                       {re}╚╗╔╝{cy}║╔╗║{re}║╔╝{cy}║╚╝║║╔╗║{re}║╔╗║{cy}
                       {re}─║║─{cy}║╚╝║{re}║║─{cy}╚╗╔╝║╔╗║{re}║╚╝║{cy}
                       {re}─╚╝─{cy}╚══╝{re}╚╝──{cy}╚╝─╚╝╚╝{re}╚══╝{cy}
                         https://github.com/Forvad"
                    '''
        )

    def setup(self):
        sleep(3)
        print(gr + "  [+] Installing  ...\n\n")
        if 'posix' in name:
            pass
        else:
                print(
                    f'''
                                          {cy}╔═══╗╔═══╗╔════╗╔╗─╔╗╔═══╗
                                          {cy}║╔═╗║║╔══╝║╔╗╔╗║║║─║║║╔═╗║
                                          {cy}║╚══╗║╚══╗╚╝║║╚╝║║─║║║╚═╝║
                                          {cy}╚══╗║║╔══╝──║║──║║─║║║╔══╝
                                          {cy}║╚═╝║║╚══╗──║║──║╚═╝║║║───
                                          {cy}╚═══╝╚═══╝──╚╝──╚═══╝╚╝───
                                          https://github.com/Forvad"
                                        '''
                )
        if 'posix' in name:
            system('''pip3 install asyncio aiohttp pyuseragents loguru urllib3 sys requests''')
        else:
            system('''pip install asyncio aiohttp pyuseragents loguru urllib3 sys requests''')



        print(gr + "[+]  Installed.\n")


Setup = Update()
settings_data = input(f"{cy}install library {gr}yes{cy} / {re}no{cy}\n Enter the: ").lower()
if settings_data in 'yes':
    Setup.setup()