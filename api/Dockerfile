FROM python:3.10.6
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install psycopg2-binary
CMD ["python", "api.py"]
EXPOSE 80
