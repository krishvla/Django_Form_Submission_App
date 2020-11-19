# Django_Form_Submission_App

---

## Overview

This is a simple Django web app that shows an example of form submission and displaying data in table..

#### This app Consists of below mentioned features.
- User Registration and Validation.
- User Authentication.
- Form Handling.
- Saving Form Data into Database.
- Working with [Messaging framework](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/) in Django.

## Installation Intsructions

Activate virtual environment if you wish.

This app installation requires [PIP](https://pip.pypa.io/en/stable/).

#### Install the dependencies and start the server.

```sh
$ cd to/this/project/directory/
$ pip install -r requirements.txt
```
#### Linking to Database.
    
- Create a postgres Database, and link it to Django Application via **settings.py** file.
- The Structure looks like this: 
--   ![Postgres DB Arch](demos/db_arch.jpg "Postgres DB Arch")

#### Running Server

```sh
$ python manage.py runserver
```

Verify the web app is working or not,  by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
or
http://localhost:8000/
```

## Snapshots

#### User Registration Page:
![Registration Page Snapshot](demos/reg.jpg "Registration Page Snapshot")

#### User Login Page:

![Login Page Snapshot](demos/login.jpg "Login Page Snapshot")

#### Form Filling Page:

![ Form Filling Page Snapshot](demos/form.jpg " Form Filling Page Snapshot")


#### Viewing Submitted Forms Page:

![Viewing Submitted Page Snapshot](demos/data.jpg "Viewing Submitted Page Snapshot")

#### Displaying Messages from Backend:

![Displaying Messages from Backend](demos/msg.jpg "Displaying Messages from Backend")

