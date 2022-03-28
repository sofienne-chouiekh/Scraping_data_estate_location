import urllib3
import requests
from bs4 import BeautifulSoup
from csv import writer
import csv
import pandas as pd

url = 'https://www.mubawab.tn/fr/cc/immobilier-a-louer-all:o:i:sc:apartments-for-rent:p:' + str(50)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
estates  = soup.find_all('li', class_='listingBox w100')
list_of_lists = []
for estate in estates:
        list_of_estate = []
        estate_local = estate.find('h3', class_='listingH3').text.split()[-1].strip()
        list_of_estate.append(estate_local)
        estate_type = "Appartement"
        list_of_estate.append(estate_type)
        estate_surface = estate.find('h4', class_='listingH4 floatR').text.split()[-2].strip()
        list_of_estate.append(estate_surface)
        estate_piece = estate.find('h4', class_='listingH4 floatR').text.split()[0].strip()
        list_of_estate.append(estate_piece)
        estate_price = getattr(estate.find("span", class_= "priceTag hardShadow float-right floatL yellowBg"),'text', None)
        if (str(estate_price)=='None'):
            estate_price = getattr(estate.find("span", class_= "priceTag hardShadow float-right floatL"),'text', None)
            list_of_estate.append(estate_price)
        else:
                list_of_estate.append(estate_price)
        list_of_lists.append(list_of_estate)
        print(estate_local + '/' + estate_type + '/' + estate_surface + '/' + estate_piece + '/' + estate_price)

df = pd.DataFrame(list_of_lists, columns=['local', 'type', 'surface', 'nb_piece', 'prix'])
df.to_csv('ziedtest.csv', index=False, sep=';')




