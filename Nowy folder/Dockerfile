FROM python:3.9


ENV APP_HOME /app


WORKDIR $APP_HOME


COPY address_book.py comands.py logic.py main.py notebook.py requirements.txt ./


RUN pip install -r requirements.txt


EXPOSE 5000


ENTRYPOINT ["python", "main.py"]