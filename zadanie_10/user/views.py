from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Quote, Author
# Create your views here.
def normalizer(text):
    normalized_text = text.replace(" ", "-").replace(".", "").replace("'", "").replace("é", "e")
    return normalized_text




def scrap_and_fill_database():

    url = 'http://quotes.toscrape.com'


    response = requests.get(url)


    if response.status_code == 200:

        authors_list = []
        page_number = 1
        while True:
            response = requests.get(f"{url}/page/{page_number}")
            soup = BeautifulSoup(response.text, "lxml")
            authors = soup.find_all("small", class_='author')
            if not authors:
                break
            for author in authors:
                name = author.text
                normalized_name = normalizer(name)
                author_url = f'{url}/author/{normalized_name}/'
                response_author = requests.get(author_url)
                soup_author = BeautifulSoup(response_author.text, 'lxml')
                description = soup_author.find('span', class_='author-description').text.strip()
                soup_author.save()
                description.save()
            page_number += 1
            return redirect(to='strona:main')
    else:

        print('Błąd: Nie udało się pobrać strony')




