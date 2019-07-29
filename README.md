# whatsonme_django_vue

## Django side

- work on virtual environment (after install anaconda)
- create a venv for the project:
    conda create --name WhatsOnME python=3.7.3
- ro show the available venvs list:
    conda info --envs
- to activate a venv:
    conda activate WhatsOnMe
- install django from conda or pip:
    conda install django

### Create a project WhatsOnMe
- create a project:
    django-admin startproject WhatsOnMe
- run the server:
     python manage.py runserver
- if error of sqlparse install it:
    pip install sqlparse
- run the server and it will be on http://127.0.0.1:8000/

### Create Auth application (service):
- python manage.py startapp Auth

