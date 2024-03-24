import lxml
import requests
from bs4 import BeautifulSoup
import json
from mongoengine import *

connect( "autorzy", host="mongoDB+SRV://pawel:<hasło>@pawel.cjlubnv.mongodb.net/?retryWrites=true&w=majority&appName=autorzy")
url=" http://quotes.toscrape.com"

def normalizer(text):
    normalized_text = text.replace(" ", "-")
    normalized_text = normalized_text.replace(".", "")
    normalized_text = normalized_text.replace("'", "")
    normalized_text = normalized_text.replace("é", "e")
    return normalized_text


class Author():
    def __init__(self):
        response= requests.get(url)
        soup=BeautifulSoup(response.text, "lxml")
        author=soup.find_all("small", class_='author')
        self.authors_list = []


        for aut in author:
            self.name=aut.text
            normalized_text=normalizer(self.name)
            self.url2 = f'{url}/author/{normalized_text}/'

            response = requests.get(self.url2)
            soup = BeautifulSoup(response.text, 'lxml')
            born = soup.find_all('span', class_='author-born-date')

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            text = soup.find_all('span', class_='text')


            for tex in text:
                self.description=tex.text
                for bo in born:

                    self.born_date=bo.text
                    authors={"fullname:": self.name,
                    "born_date:": self.born_date,
                    "description": self.description}
                    self.authors_list.append(authors)



author= Author()


with open("authors.json", "w") as f:
        json.dump(author.authors_list, f, indent=4)
        f.write("\n")