import requests
from colorama import init, Fore

# Colorama init
init()

# Input for Account Creation.
username = input(f'{Fore.LIGHTMAGENTA_EX}Username: ')
password = input(f'{Fore.LIGHTWHITE_EX}Password: ')
email = input(f'{Fore.LIGHTCYAN_EX}Email: ')

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "birth_day": "02",
    "birth_month": "08",
    "birth_year": "2000",
    "collect_personal_info": "undefined",
    "creation_flow": "",
    "creation_point": "https://www.spotify.com/us/",
    "displayname": username,
    "email": email,
    "gender": "male",
    "iagree": "1",
    "key": "a1e486e2729f46d6bb368d6b2bcda326",
    "password": password,
    "password_repeat": password,
    "platform": "",
    "send-email": "0",
    "thirdpartyemail": "0",
    "fb": "0",
    "username": username,
}  # DONT CHANGE

resp = requests.post("https://spclient.wg.spotify.com/signup/public/v1/account"
                     )  # Account Creation
if resp.status_code == 1:
    print(f'{Fore.LIGHTGREEN_EX}Account Created\nLogin: {Fore.LIGHTBLUE_EX}{username}:{Fore.LIGHTBLACK_EX}{password}')
else:
    print(f'{Fore.LIGHTRED_EX}You got a error! please open issue on GitHub or try with other name and/or email')
