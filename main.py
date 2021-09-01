import requests, os
from colorama import Fore, init
def pse():
    os.system('pause')
pse()
init()
username = input(f'{Fore.LIGHTMAGENTA_EX}Username: {Fore.RESET}')
email = input(f'{Fore.LIGHTMAGENTA_EX}Email: {Fore.RESET}')
password = input(f'{Fore.LIGHTMAGENTA_EX}Password: {Fore.RESET}')

resp = requests.post("https://spclient.wg.spotify.com/signup/public/v1/account", data={
    "birth_day": "1",
    "birth_month": "01",
    "birth_year": "1970",
    "collect_personal_info": "undefined",
    "creation_flow": "",
    "creation_point": "https://www.spotify.com/uk/",
    "displayname": username,
    "username": username,
    "gender": "neutral",
    "iagree": "1",
    "key": "a1e486e2729f46d6bb368d6b2bcda326",
    "platform": "www",
    "referrer": "https://www.spotify.com/uk/",
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
})

resp = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', data=data)
if "login_token" in resp.text:
    print(f'{Fore.LIGHTGREEN_EX}Account Created\nLogin: {Fore.LIGHTBLUE_EX}{username}:{Fore.LIGHTBLACK_EX}{password}\nResponse: {resp.text}')
    pse()

elif "That email is already" or "Invalid Email" in resp.text:
    print(f'{Fore.LIGHTRED_EX}You got an error! Please try using a different email\nResponse: {resp.text}')
    pse()

else:
    print(f'{Fore.LIGHTRED_EX}You got an error! Try with a different username and/or disable your proxy/VPN. If that doesn\'t work, please open issue on GitHub \nResponse: {resp.text} \n {resp.status_code}')
    pse()
