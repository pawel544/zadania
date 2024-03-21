from mongoengine import *
import json

connect( "autorzy", host="mongoDB+SRV://pawel:<hasło>@pawel.cjlubnv.mongodb.net/?retryWrites=true&w=majority&appName=autorzy")

class Autor(Document):
    name=StringField(required=True)
class Quate(Document):
    text=StringField(required=True)
    author=StringField(Autor)
    tag=ListField(StringField())
class import_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            author_name = entry['author']
            author = Autor.objects(name=author_name).first()
            if not author:
                author = Autor(name=author_name)
                author.save()

            quote = Quate(
                text=entry['quote'],
                author=author,
                tags=entry['tags']
            )
            quote.save()
def search_quotes(criteria):
    if criteria.startswith('name:'):
        author_name = criteria.split(':')[-1].strip()
        author = Autor.objects(name=author_name).first()
        if author:
            quotes = Quate.objects(author=author)
            print_quotes(quotes)
        else:
            print("No quotes found for the author.")

    elif criteria.startswith('tag:'):
        tag = criteria.split(':')[-1].strip()
        quotes = Quate.objects(tags=tag)
        print_quotes(quotes)

    elif criteria.startswith('tags:'):
        tags = criteria.split(':')[-1].strip().split(',')
        quotes = Quate.objects(tags__in=tags)
        print_quotes(quotes)

    elif criteria == 'exit':
        print("Exiting the script.")
        exit()

    else:
        print("Invalid command. Please try again.")

def print_quotes(quotes):
    for quote in quotes:
        print(f'Author: {quote.author.name} - Quote: {quote.text}')


def main():
    while True:
        command = input("Enter command (name: <author_name>, tag: <tag>, tags: <tag1>,<tag2>, ..., exit): ")
        search_quotes(command)

if __name__ == "__main__":
    main()