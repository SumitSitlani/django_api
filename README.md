# django_test

This is basic Django application that allows the user to add data into database and show the database. 
Using the custom forms the user can enter the data and using the template the user can view the data.
Using Django Rest Framework I have added basic API crud operations for the user endpoints.

The endpoints are listed below"

open your browser and go to the following link:

http://localhost:8000/api/

Here in this app the links are provided to acces the API's where user can :
1. Add the data(user data) using API
2. Update the data using API
3. View the list of users 
4. View the details of an individual user using ID
5. Delete the user using API

```
{
    "List": "/user-list/",
    "Details View": "/user-list/<str:pk>/",
    "Create": "/user-create/",
    "Update": "/user-update/<str:pk>/",
    "Delete": "/user-delete/<str:pk>/"
}
```

# Installation

Clone the project to your desktop and configure the database settings in the **settings.py** file.(For this project I have used MySQL as my databse).

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER':'root',
        'PASSWORD':'password',
        'NAME':'django_test',
        'PORT':3306
    }
}
```

After configuring the database open the terminal and write
`python manage.py runserver`

and open the browser and go to 

http://localhost:8000

and for api app go to 

http://localhost:8000/api/


**NOTE** : I havent used validations in this project and have not focused on the UI of the app. This app is just for making the API endpoints and applying CRUD operations using Django Rest Framework
