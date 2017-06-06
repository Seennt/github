# A personal development repository.

This repo is for development and testing purpose.

# Requirements
- Install python 3.6.1
- Install postgresql
- pip install Django
- django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile {{ project_name }}

In this case a Django project is created based on the system Interpreter. After creating a "virtual environment" the correct Interpreter
must be configured in PyCharm.
- virtualenv virtual
- cd {{ project_name }}
- virtual\Scripts\activate.bat
- pip install -r requirements.txt

# Deployment to Heroku
=======

This repo is for development and testing purpose.

## Requirements

- Install python 3.6.1
- Install postgresql 
- virtualenv virtual
- virtual\Scripts\activate.bat
- pip install Django

- django-admin startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile {{ project_name }}

- virtual\Scripts\deactivate.bat

- move virtual {{ project_name }}\virtual

- virtual\Scripts\activate.bat

## Deployment to Heroku

    $ git init
    $ git add -A
    
    $ git remote add github https://github.com/Seennt/github.git
    $ git remote -v
    $ git commit -m "Initial commit"
    $ heroku create seennt --region eu
    $ git remote -v
    $ git push heroku master
    
    $ git push github master
    # Now go to heroku dashboard an configure deployment via github.
    
## Install papertrail addon

    heroku addons:create papertrail

# License
MIT

# Pycharm
Rename interpreter to: Virtual-environment-Python-3.6.1

- Add .idea to .gitignore
- Would you like to add universioned to .gitignore? cancel

## Terminal
- Change the default parameter format to in case of psql: chcp 1252

Reroute project directory: trl+alt+s -> tools -> terminal, set project-path:

    mklink /J "C:/Users/<username>/Amazon drive/<project_name>" C:/Users/<username>/<project_name>
     
Therefor:

    C:/Users/<username>/Projects/<project_name>

# PostgreSQL
As a best-practise installing PostgreSQL local requires:
    
    set PGUSER=postgres
    set PGPASSWORD=<passwd>
    set DATABASE_URL=postgresql://localhost:5432/postgresql-animated-51412

Within this structure 2 databases are installed. One local PostgreSQL and one remote Heroku-PostgreSQL database. 
For now development is done at a windows machine, meaning that
    
    heroku pg:push 
    heroku pg:pull

Reply with the following:
    
    'env' is not recognized as an inpipternal or external command, operable program or batch file.

# Frontend
This seennt platform will be equipped with the Django Template language(DTL) in combination with:
- HTML 5 Boilerplate
- Bootstrap 3

Don't start from scratch start with [initializr](http://www.initializr.com/)

## HTML 5 Boilerplate
The focus is on the backend, nevertheless DRY coding is still preferred as 
[a best practise](http://www.marinamele.com/2014/02/django-best-practices-ii-project.html) for creating a 
project structure.

## Bootstrap 3

## License: MIT

## Pycharm:
Rename interpreter to: Virtual environment <Version no.>

Reroute project directory: trl+alt+s -> tools -> terminal, set project-path:

    "mklink /J "C:/Users/<username>/Amazon drive/<project_name>" C:/Users/<username>/<project_name>"
Therefor:

    C:/Users/<username>/Projects/<project_name>
    
- Add .idea to .gitignore
- Would you like to add universioned to .gitignore? add