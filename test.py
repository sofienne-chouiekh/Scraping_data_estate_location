import urllib3
import requests
from bs4 import BeautifulSoup
from csv import writer
import csv
import pandas as pd

url = 'https://www.mubawab.tn/fr/cc/immobilier-a-louer-all:o:i:sc:houses-for-rent:p:' + str(1)
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists  = soup.find_all('li', class_='listingBox w100')
for list in lists:
            estate_local = list.find('h3', class_='listingH3').text.split()[-1].strip()
            estate_type = "Maison"
            estate_surface = getattr(list.find('h4', class_='listingH4 floatR'),'text', None)
            estate_piece = list.find('h4', class_='listingH4 floatR').text.split()[0].strip()
            estate_price = getattr(list.find("span", class_= "priceTag hardShadow float-right floatL yellowBg"),'text', None)
            if (str(estate_price)=='None'):
                estate_price = getattr(list.find("span", class_= "priceTag hardShadow float-right floatL"),'text', None)
            info = [estate_local, estate_type, estate_surface, estate_piece, str(estate_price)]
            print(info)








