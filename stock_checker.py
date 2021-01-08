import json
import requests
import smtplib, ssl

f = open('./config.json', 'r')
config = json.load(f)

items = config['items']

message = ''

for item in items:
    url = item['url']
    resp = requests.get(url)
    webpage = resp.text
    name = item['name']
    if 'out of stock' not in webpage.lower():
        message = f'{message}\n Name: {name} \n {url}'


port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

if len(message) > 0:
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        server.login("out.of.stock.checker.bot@gmail.com", 'indian41')
        people = config['people']
        for person in people:
            receiver = person['email']
            sender = 'out.of.stock.checker.bot@gmail.com'
            server.sendmail(sender, receiver, f'Subject: Items in Stock!\n\n{message}')
    except:
        print('mer')
