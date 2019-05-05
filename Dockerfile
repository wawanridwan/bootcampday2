From python:3.6.5-alpine

WORKDIR /code

COPY ./requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code

CMD ["python", "manage.py", "runserver"]
