import requests, bs4

url_NYT = 'https://www.nytimes.com'

r = requests.get(url_NYT)

r_html = r.text

print(r_html)