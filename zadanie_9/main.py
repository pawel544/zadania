import lxml
import requests
from bs4 import BeautifulSoup
import json
from mongoengine import connect


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
    page = 1
    soup = BeautifulSoup(response.text, "lxml")
    author = soup.find_all("small", class_='author')
    for aut in author:
        name=aut.text

        normalized_text=normalizer(name)
        url2 = f'{url}/author/{normalized_text}/'
        response1 = requests.get(url2)
        soup1 = BeautifulSoup(response1.text, "lxml")
        born = soup1.find_all('span', class_='author-born-date')
        for bo in born:
            born_date=bo.text

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
            for bo in born:
                print(bo)
                born_date = bo.text
                authors={"fullname:": name,
                "born_date:": born_date}
                authors_list.append(authors)
        page+=1


    return authors_list


def quatos(url):

    qoutes_list=[]
    page = 1
    response = requests.get(url)
    soup1 = BeautifulSoup(response.text, "lxml")
    text = soup1.find_all('span', class_='text')
    for tex in text:
        description = tex.text
    while True:

        url3 = f"{url}/page/{page}"
        response1 = requests.get(url3)
        soup1 = BeautifulSoup(response1.text, "lxml")
        text = soup1.find_all('span', class_='text')

        for tex in text:
            description = tex.text
            
        if not description:
            break
            soup = BeautifulSoup(response.text, "lxml")
            born = soup.find_all('span', class_='author-born-date')
            text = soup1.find_all('span', class_='text')

        for tex in text:
                description=tex.text



                qoutes = {"qoutes": description}


                qoutes_list.append(qoutes)
        page +=1
    return qoutes_list



qoutes_data=quatos(url)
authors_data=author(url)
print("Proces zakończony Sukcesem")
with open("authors.json", "w") as f:
        json.dump(authors_data, f, indent=4)
        f.write("\n")
with open("qoutes.json", "w") as f:
    json.dump(qoutes_data, f, indent=4)
    f.write("\n")