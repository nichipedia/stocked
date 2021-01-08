import requests
from bs4 import BeautifulSoup
import smtplib, ssl

url = 'https://www.midwayusa.com/product/1023130090?pid=697097'

resp = requests.get(url)
webpage = resp.text

print('out of stock' not in webpage.lower())

