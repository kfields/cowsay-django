# The Making of Cowsay-Django

There are a lot of ways to structure a Django project.
My goal here is to find a way that involves the least amount of manual reorganization.

## Create Project

```bash
hatch new cowsay-django
```

## Add Stuff
...


```bash
hatch shell
```

## Create Test Django Site

```bash
django-admin startproject mycowsay .
```

This creates the project in the current directory, else you will get a parent directory with the same name.  Undesirable.

## Create Django App

```bash
cd src/cowsay_django
```

```bash
../../manage.py startapp cowsayer
```

Can't use cowsay because it conflicts with existing Python module.

### Modify apps.py
    name = 'cowsay_django.cowsayer'

```bash
cd ../..
```

## Make and Apply Migrations

```bash
./manage.py makemigrations
./manage.py migrate
```
## Make Template Tags

Restart the server!

## Run Server

```bash
./manage.py runserver
```