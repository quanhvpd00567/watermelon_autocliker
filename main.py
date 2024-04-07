
import requests
import json
URL = "https://arbuz.betty.games/api/click/apply"
 
headers = {
  'authority': 'arbuz.betty.games',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
  'content-type': 'application/json',
  'dnt': '1',
  'origin': 'https://arbuzapp.betty.games',
  'referer': 'https://arbuzapp.betty.games/',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'x-telegram-init-data': 'user=%7B%22id%22%3A1482439973%2C%22first_name%22%3A%22Qu%C3%A2n%22%2C%22last_name%22%3A%22Ho%C3%A0ng%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=-732709353687537597&chat_type=channel&start_param=ref_Dgbopb3w_squad_mineHOT100do&auth_date=1712414566&hash=ba15ede148e29b3758c49d262dd0a95627e4903a92bb732af9609762b14cb34e'
}
 
# defining a params dict for the parameters to be sent to the API
payload = json.dumps({
  "count": 200,
  "hash": "7f95c1c3a069e76f61b2f91b2c0ca6fde55b8d887c15169237260819ac3f84bf"
})
 
# sending get request and saving the response as response object
response = requests.request("POST", URL, headers=headers, data=payload)
 
# extracting data in json format
# data = r.json()
if response.status_code == 200:
  dataJson = response.json();
  print(dataJson)
print(response.status_code);