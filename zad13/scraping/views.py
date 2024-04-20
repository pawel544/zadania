from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from .models import Quote, Author
# Create your views here.
def normalizer(text):
    normalized_text = text.replace(" ", "-").replace(".", "").replace("'", "").replace("é", "e")
    return normalized_text




def scrap_and_fill_database(request):
    if request.method == "POST":


        url = 'http://quotes.toscrape.com'






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

                description_1 = soup_author.find('span', class_='author-description')
                if description_1:
                    description= description_1.text.strip()
            page_number += 1
            return redirect(to='strona:main')
    else:

        print('Błąd: Nie udało się pobrać strony')




