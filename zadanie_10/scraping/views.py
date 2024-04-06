from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Quote, Author
# Create your views here.
def scrap_and_fill_database():

    url = 'http://quotes.toscrape.com'


    response = requests.get(url)


    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')


        items = soup.find_all('div', class_='item')


        for item in items:

            title = item.find('h2').text
            description = item.find('p').text


            my_model_instance = MyModel(title=title, description=description)
            my_model_instance.save()
    else:

        print('Błąd: Nie udało się pobrać strony')


scrap_and_fill_database()

