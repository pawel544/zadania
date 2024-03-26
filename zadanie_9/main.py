import lxml
import requests
from bs4 import BeautifulSoup
import json
from mongoengine import connect

connect( "autorzy", host="mongoDB+SRV://pawel:<hasło>@pawel.cjlubnv.mongodb.net/?retryWrites=true&w=majority&appName=autorzy")
url=" http://quotes.toscrape.com"

def normalizer(text):
    normalized_text = text.replace(" ", "-")
    normalized_text = normalized_text.replace(".", "")
    normalized_text = normalized_text.replace("'", "")
    normalized_text = normalized_text.replace("é", "e")
    return normalized_text

class Name():
    pass
class Born_name():
    pass
class description():
    pass

def author(url):
    response = requests.get(url)
    authors_list = []
    soup = BeautifulSoup(response.text, "lxml")
    author = soup.find_all("small", class_='author')
    for aut in author:

        name=aut.text
        normalized_text=normalizer(name)
        url2 = f'{url}/author/{normalized_text}/'
        response1 = requests.get(url2)
        soup1 = BeautifulSoup(response1.text, "lxml")
        born = soup1.find_all('span', class_='author-born-date')
        text = soup.find_all('span', class_='text')
        for tex in text:
         description=tex.text
        for bo in born:


            born_date=bo.text
            authors={"fullname:": name,
            "born_date:": born_date,
            "description": description}
            authors_list.append(authors)
    return authors_list


def page(author1):
    authors_list = []
    page = 1
    while True:
        url3 = f"{url}/page/{page}"
        response1 = requests.get(url3)


        soup1 = BeautifulSoup(response1.text, "lxml")
        author = soup1.find_all("small", class_='author')
        if not author:
            break

        for aut in author:

            name = aut.text
            normalized_text = normalizer(name)
            url2 = f'{url}/author/{normalized_text}/'
            response = requests.get(url2)
            soup = BeautifulSoup(response.text, "lxml")
            born = soup.find_all('span', class_='author-born-date')
            text = soup1.find_all('span', class_='text')

        for tex in text:
         description=tex.text

         for bo in born:

                born_date=bo.text
                authors={"fullname:": name,
                "born_date:": born_date,
                "description": description}
                authors_list.append(authors)

        page +=1
    return authors_list



author1 = author(url)
authors_data=page(author1)
print("Proces zakończony Sukcesem")
with open("authors.json", "w") as f:
        json.dump(authors_data, f, indent=4)
        f.write("\n")