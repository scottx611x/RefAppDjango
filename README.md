# RefAppDjango
Same project as before, but implemented in Django rather than Flask

##Install instructions:
```bash

pip install virtualenv

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install postgresql

postgres -D /usr/local/var/postgres

edit user and pass in DATABASES in settings.py

createdb <db_name>

git clone https://github.com/scottx611x/RefAppDjango.git

cd RefAppDjango

virtualenv venv

. venv/bin/activate

pip instll django

pip install psycopg2

python manage.py migrate

python manage.py runserver

```
