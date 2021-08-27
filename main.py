import requests, colorama

# main stuff.
username = input('Username: ')
password = input('Password: ')
email = input('Email: ')

headers = {
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
}

resp = requests.post("https://spclient.wg.spotify.com/signup/public/v1/account")
if resp.status_code == 1:
    print(f'Account Created\nLogin: {username}:{password}')
else:
    print('bye bye!')