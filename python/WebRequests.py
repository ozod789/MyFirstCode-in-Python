import requests

page = requests.get('https://www.google.com')
print(page.status_code)
print(page.text)