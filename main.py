import requests
from colorama import Fore, init
init()
username = input(f'{Fore.LIGHTMAGENTA_EX}Username: {Fore.RESET}')
email = input(f'{Fore.LIGHTMAGENTA_EX}Email: {Fore.RESET}')
password = input(f'{Fore.LIGHTMAGENTA_EX}Password: {Fore.RESET}')

data = {
    "birth_day":             "1",
    "birth_month":           "01",
    "birth_year":            "2000",
    "collect_personal_info": "undefined",
    "creation_point":        "https://www.spotify.com/us/",
    "displayname":           username,
    "email":                 email,
    "gender":                "male",
    "iagree":                "1",
	"key":                   "a1e486e2729f46d6bb368d6b2bcda326",
	"password":              password,
	"password_repeat":       password,
	"username":              username,
}

resp = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', data=data)
if "\"login_token\"" in resp:
    print(f'{Fore.LIGHTGREEN_EX}Account Created\nLogin: {Fore.LIGHTBLUE_EX}{username}:{Fore.LIGHTBLACK_EX}{password}\nResponse: {resp.text}')

elif "That email is already" or "Valid Email" in resp:
    print(f'{Fore.LIGHTRED_EX}You got a error! Please try using other email\nResponse: {resp.text}')
else:
    print(f'{Fore.LIGHTRED_EX}You got a error! please open issue on GitHub or try with other name and/or disable proxy/VPN\nResponse: {resp.text}')
