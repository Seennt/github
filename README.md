# A personal development repository.

This repo is for development and testing purpose.

# Project documentation
A structured manner to write documentation for the platform and each individual application.

## Production & Development
Production settings:
 - ALLOW_HOST
 - DEBUG
 
The gap between production and development should be a small as possible. Via GIT
version control is maintained. So code can be converted back. 

- A stable commit **Version: v0.1: Standby release**

#### Database
In relation to production & development gap, a proper workflow should be defined how to 
maintain reliable database information.

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

## Deployment to Heroku via GITHUB

    $ git init
    $ git add -A
    
    $ git remote add github https://github.com/Seennt/system.git
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
- Change the console page code to 1252 so psql is compatible with UTF-8. this can be done via: chcp 1252. 
(Is set via setpsql.bat)

Reroute project directory: ctrl+alt+s -> tools -> terminal, set project-path:

    mklink /J "C:/Users/<username>/Amazon drive/<project_name>" C:/Users/<username>/<project_name>
     
Therefor:

    C:/Users/<username>/Projects/<project_name>

# PostgreSQL
As a best-practise installing PostgreSQL local requires:
    
    set PGUSER=postgres (Is set via setpsql.bat)
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
- HTML 5 Boilerplate structure
- Bootstrap 3
- Bootstrap sass

## Favicon
Generate a favicon online for instance [here](http://realfavicongenerator.net/).

## HTML 5 Boilerplate
The focus is on the backend, nevertheless DRY coding is still preferred as 
[a best practise](http://www.marinamele.com/2014/02/django-best-practices-ii-project.html) for creating a 
project structure.

## Bootstrap 3
Seennt system is equipped with bootstrap3 and bootstrap3-sass, to compile sass django_compressor is required.

- To optimize the frontend combine bootstrap3 with Django Template Language. 
- Separate bootstrap3 in templates per function.
    
#### SASS
To compress SASS via django-compressor make sure compress_offline is set in settings.py. Furthermore configure
post_compile is installed according [heroku django cookbook](https://github.com/nigma/heroku-django-cookbook).

- As a remark: Static folder should be managed correctly.

## License: MIT

## Pycharm:
Rename interpreter to: Virtual environment <Version no.>

Reroute project directory: CTRL+ALT+S > tools > terminal, set project-path:

    "mklink /J "C:/Users/<username>/Amazon drive/<project_name>" C:/Users/<username>/<project_name>"
Therefor:

    C:/Users/<username>/Projects/<project_name>
    
- Add .idea to .gitignore
- Would you like to add universioned to .gitignore? add
