# README

## About Fizz Buzz Game

[Fizz buzz](https://en.wikipedia.org/wiki/Fizz_buzz) is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", and any number divisible by five with the word "buzz".

## Project

The project implements the Fizz Buzz game in terms of online API's. User makes a `GET` request to an API endpoint with a number to find out if a number is Fizz, Buzz, or FizzBuzz. The user gets a result in return in terms of API response.

With this application, it is also possible to change the keywords 'Fizz', 'Buzz', and counters with separate API endpoints to make this game challenging.

## Prerequisite

To compile this project you need:

- `python3`
- `pip3`

## Installation Steps

#### Step 1:

Clone git repository

`git clone git@github.com:ashish-jadhav/FizzBuzz.git`

Open directory with cd command

`cd FizzBuzz`

#### Step 2:

Create a virtual environment and install packages from requirements.txt file

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Step 3:

Make migrations

`python manage.py makemigrations`

Migrate

`python manage.py migrate`

#### Step 4:

Run Django web server. Django web server will start on port 8000 by default.

`python manage.py runserver`

## Database

SQLite database is used in this example. It is recommended to use PostgreSQL in production.

## Examples

#### GET request with a number:

REQUEST: `GET http://localhost:8000/fizzbuzz/1/` JSON response: `{"result":"1"}`

REQUEST: `GET http://localhost:8000/fizzbuzz/3/` JSON response: `{"result":"Fizz"}`

REQUEST: `GET http://localhost:8000/fizzbuzz/5/` JSON response: `{"result":"Buzz"}`

REQUEST: `GET http://localhost:8000/fizzbuzz/15/` JSON response: `{"result":"FizzBuzz"}`

REQUEST: `GET http://localhost:8000/fizzbuzz/00/` JSON response: `{"result":"invalid input"}`

#### PATCH request to change key and values:

By default, the application uses keys as Fizz, Buzz, and values 3, 5 respectively.
Key values can easily be changed by making a `PATCH` request.

REQUEST: `PATCH http://localhost:8000/fizzbuzz/change/` JSON response: `{"result":"success"}`

HEADERS: `Content-Type: application/json`

BODY:

```json
{
  "fizz_name": "Foo",
  "fizz_count": "4",
  "buzz_name": "Bar",
  "buzz_count": "10"
}
```

Check if the `GET` request is working properly

REQUEST: `GET http://localhost:8000/fizzbuzz/40/` JSON response: `{"result":"FooBar"}`

It is possible to change only one or more values as shown below.
BODY:

```json
{
  "buzz_name": "Bar"
}
```

#### ERROR:

For any invalid input user gets a response as below.

```json
{
  "result": "invalid input"
}
```
