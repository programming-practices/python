import requests
url = "https://es.wikipedia.org/wiki/Vicente_del_Bosque"
webConnect = requests.get(url)
# print(webConnect.status_code)
# print(webConnect.text)
print(type(webConnect.text))