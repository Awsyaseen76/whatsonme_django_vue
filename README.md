# whatsonme_django_vue

## Django side

- work on virtual environment (after install anaconda)
- create a venv for the project:
    `conda create --name WhatsOnME python=3.7.3`
- ro show the available venvs list:
    `conda info --envs`
- to activate a venv:
    `conda activate WhatsOnMe`
- install django from conda or pip:
    `conda install django`
- install django REST framework
    `pip install djangorestframework`

## Create a project WhatsOnME
- create a project:
    `django-admin startproject WhatsOnME`
- run the server:
     `python manage.py runserver`
- if error of sqlparse install it:
    `pip install sqlparse`
- run the server and it will be on http://127.0.0.1:8000/


### MySql connection
- install pymysql: -->  pip install pymysql
- on project __init__.py:
    `import pymysql `
    `pymysql.install_as_MySQLdb()`
- connect to the database on the settings.py file
- create the database on mysql with the name provided in the settings above

- for the error of:
    `django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.`
    solve it as the stackoverflow:
    '''
        Go to your django/db/backends/mysql installation dir. Check your path in the error message.

        the path is: 
        /anaconda3/envs/WhatsOnME/lib/python3.7/site-packages/django/db/backends/mysql

        Open file base.py and search for:
        `version = Database.version_info`
        Put a pass inside if and comment line:

        `raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.version)
        Like this.`

        `if version < (1, 3, 13):`
        `pass`
        '''
        raise ImproperlyConfigured(
            'mysqlclient 1.3.13 or newer is required; you have %s.'
            % Database.__version__
        )
        '''
        Save, close this file and open operations.py.

        Search for:

        `query = query.decode(errors='replace')`
        and change decode to encode

        `query = query.encode(errors='replace')`
        Now, try to run the server.
    '''

### Create a super user for admin page
- migrate the models for the user setting
    `python manage.py migrate`
- create a super user
    `python manage.py createsuperuser`
    username, email, password
- now `http://127.0.0.1:8000/admin/` is working


### Create Auth application (service):
- `python manage.py startapp Auth`
- add the app name to: WhatsOnME/settings.py -> INSTALLED_APPS
- on the project's url.py:
    imoprt 'include'
    create a path for the app (service) that point to the app (Auth's urls.py)
    so each request comes to the auth_api/ pipe it to the urls for that service
- on the app (service) create the urls.py file that contains the internal paths and:
    import path and the views file for the app (service)
    create the urlpatterns containing the paths and pipe it for corresponding view
- 

### Using Django REST framework:
- using the serilizer to convert the return object from the model to JSON and vice versa when creating new record
    `pip install djangorestframework` if not installed before as on the first step
- add it to the settings -> INSTALLED_APPS:
    `'rest_framework',`

### Setting up CORS
- `pip install django-cors-headers`
- used to determine the whitelist that can be accessed
- on the settings.py file:
    . on the INSTALLED _APPS -> add 'corsheaders'
    . on MIDDLEWARE add:
        `'corsheaders.middleware.CorsMiddleware',`
        `'django.middleware.common.CommonMiddleware',`
    . then setup CORS after MIDDLEWARE:
        `CORS_ORIGIN_ALLOW_ALL = False`
        `CORS_ORIGIN_WHITELIST = (`
            `'http://localhost:4200',`
        `)`

### Create the data model for Auth
- on Auth -> models.py: create the Auth model
- migrate the created model:
    the 'Auth' below is the app(service) name without specific name it will migrate all applications
    `python manage.py makemigrations Auth`
    `python manage.py migrate Auth`
- now the table 'Auth' has been created.

### Using the Serialization
- It used to serialization to JSON and deserialization from JSON for the model instance that created and returned.
- This AuthSerializer will inherit from rest_framework.serializers.ModelSerializer superclass.
- ModelSerializer class automatically populates a set of default fields and default validators, we only need to specify the model class.

### Create the views and urls files:
- create the views.py for the Auth app including:
    '''
    GET     Auths/: get all Auths
    GET     Auths/user_name: find Auth by user_name
    POST    Auths/: save an auth
    GET     Auths/id: get an auth by id
    PUT     Auths/id: update a auth by id
    DELETE  Auths/id: delete a auth by id
    '''

### using the admin page:
- to show the model on the admin page:
    - on admin.oy file import the model and:
        `admin.site.register(Auth)`


## the server running on http://127.0.0.1:8000











## Vue side
- `vue create auth`
- `npm install axios`
- `npm install vue-router`
- create the file .jshintrc on the root to use the es6
- run the app:
    `npm run serve`
    it works on http://localhost:8080
- on src/main.js:
    import router and use it
- create the file http-common.js it will glue the vue with the django:
    import axios
    create axios and set the base url 'http://localhost:8000/auth_api'
- on the file vue.config.js:
    Set the port for 4200 that match the port on CORS settings in django in the CORS_ORIGIN_WHITELIST

### Creating the components:

1. auth_list
2. auth_details
3. add_auth
4. search_auth

### Create the router:

## Now Vue has been connected to Django succussfully :)

