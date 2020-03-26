# Casting Agency API Backend - Capstone

## Introduction

The Casting Agency models a company that is responsible for producing songs and managing and assigning artists to play songs. You are a manager within the company and are creating a system to simplify and streamline your process. 

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup

To test endpoints, with Postgres running, restore a database using the castingagency.sql file provided. From the file directory in terminal run:
```bash
psql castingagency < castingagency.sql
```

## Running the server

From within the file directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python3 app.py
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `add:artists`
    - `add:songs`
    - `delete:artists`
    - `delete:songs`
    - `edit:artists`
    - `edit:songs`
    - `view:artists`
    - `view:songs`
6. Create new roles for:
    - Casting Assistant
        - Can view artists and songs
    - Casting Manager
        - All permissions 
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users - assign the Casting Assistant role to one    and Casting Director role to another, and Executive Producer   to the other.
    - Sign into each account and make note of the JWT.
    - Test each endpoint and correct any errors.

## Demo Page  

https://casting-agency-capstone-shimin.herokuapp.com/

Test each endpoint with the link above ,and different role's Jwts. 
JWTs for different role can be accessed by login to the link with username and password provided as follows.
https://shiminlei.auth0.com/authorize?audience=castingAgency&response_type=token&client_id=E3HWwWbxrsO0CZ7ENyvQV84UyU9pm8Jd&redirect_uri=http://localhost:8100/

```
- Casting Assistant
    - UserName: assistant@castingagency.com
    - Password: Udacity!@# 
- Casting Manager
    - UserName: manager@castingagency.com
    - Password: Udacity!@# 
```

## Endpoints documentation

#### `GET '/songs'`
- Fetches a dictionary of songs
- Required URL Arguments: None
- Required Data Arguments: None
- Returns: Returns Json data about songs 
- Success Response:
```
{
    "songs": [
        {
            "gente": "Blue",
            "id": 1,
            "release_date": "Thu, 01 Aug 2002 00:00:00 GMT",
            "title": "Water"
        }
    ],
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `GET '/artists'`
- Fetches a dictionary of artists
- Required Data Arguments: None
- Returns: Json data about artists
- Success Response:
```
{
    "artists": [
        {
            "age": 18,
            "gender": "other",
            "id": 1,
            "name": "Penny"
        }
    ],
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `DELETE '/songs/<int:song_id>'`
- Deletes the `song_id` of song
- Required URL Arguments: `song_id: song_id_integer` 
- Required Data Arguments: None
- Returns: Json data about the deleted song's ID 
- Success Response:
```
{
    "id_deleted": 5,
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `DELETE '/artists/<int:artist_id>'`
- Deletes the `artist_id` of artist
- Required URL Arguments: `artist_id: artist_id_integer` 
- Required Data Arguments: None
- Returns: Json data about the deleted artist's ID 
- Success Response:
```
{
    "id_deleted": 4,
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```


#### `POST '/songs'`
- Post a new song in a database.
- Required URL Arguments: None 
- Required Data Arguments:  Json data                
- Success Response:
```
{
    "song": {
        "id": 6,
        "genre": "Blue",
        "release_date": "Thu, 01 Aug 2002 00:00:00 GMT",
        "title": "Love Song"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `POST '/artists'`
- Post a new artist in a database.
- Required URL Arguments: None 
- Required Data Arguments:  Json data   

- Success Response:
```
{
    "artist": {
        "age": 18,
        "gender": "male",
        "id": 4,
        "name": "Mike"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```


#### `PATCH '/songs/<int:song_id>'`
- Updates the `song_id` of song
- Required URL Arguments: `song_id: song_id_integer` 
- Required Data Arguments: None
- Returns: Json data about the updated song 
- Success Response:
```
{
    "song": {
        "id": 5,
        "genre": "Blue",
        "release_date": "Wed, 05 Dec 2018 00:00:00 GMT",
        "title": "Love Song"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

#### `PATCH '/artists/<int:artist_id>'`
- Updates the `artist_id` of artist
- Required URL Arguments: `artist_id: artist_id_integer` 
- Required Data Arguments: None
- Returns: Json data about the deleted artist's ID 
- Success Response:
```
{
    "artist": {
        "age": 28,
        "gender": "other",
        "id": 4,
        "name": "Penny"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```

## Testing
For testing, required jwts are included for each role.
To run the tests, run
```
python3 test_app.py
```


