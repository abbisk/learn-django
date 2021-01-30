# learn-django

# Quick Setup (Terminal commands)

## Install pip first
> sudo apt-get install python3-pip

## Install virtual environment using pip3
> sudo pip3 install virtualenv

## Now create a virtual environment
> virtualenv -p python3 venv

## To activate virtual environment
> source venv/bin/activate

## Install requirements
> pip install -r requirements.txt

## make migrations
> python manage.py makemigrations

## migrate
> python manage.py migrate

## run server
> python manage.py runserver

## Deactivate virtual environment
> deactivate
