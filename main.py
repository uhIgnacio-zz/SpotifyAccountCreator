import requests
import os
from colorama import Fore, init


def Clear():
    os.system("cls" if os.name == "nt" else "clear")


Clear()

init()
username = input(f'{Fore.LIGHTMAGENTA_EX}Username: {Fore.RESET}')
email = input(f'{Fore.LIGHTMAGENTA_EX}Email: {Fore.RESET}')
password = input(f'{Fore.LIGHTMAGENTA_EX}Password: {Fore.RESET}')

resp = requests.post("https://spclient.wg.spotify.com/signup/public/v1/account", data={
    "birth_day": "29",
    "birth_month": "06",
    "birth_year": "2000",
    "collect_personal_info": "undefined",
    "creation_flow": "",
    "creation_point": "https://www.spotify.com/cl/",
    "displayname": username,
    "username": username,
    "gender": "neutral",
    "iagree": "1",
    "key": "a1e486e2729f46d6bb368d6b2bcda326",
    "platform": "www",
    "referrer": "",
    "send-email": "0",
    "thirdpartyemail": "0",
    "email": email,
    "password": password,
    "password_repeat": password
}, headers={
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "referer": "https://www.spotify.com/",
    "referrer-policy": "strict-origin-when-cross-origin"
}).json()

if "\"login_token\"" in resp:
    print(f'{Fore.LIGHTGREEN_EX}Account Created\nLogin: {Fore.LIGHTBLUE_EX}{username}:{Fore.LIGHTBLACK_EX}{password}')
elif "That email is already" in resp:
    print(f'{Fore.LIGHTRED_EX}You got a error! Please try using other email')
else:
    print(f'{Fore.LIGHTRED_EX}You got a error! please open issue on GitHub or try with other name and/or disable proxy/VPN')
    
