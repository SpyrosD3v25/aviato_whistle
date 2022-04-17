# Aviato

Aviato is a whistle-blow platform that is build for citizens.

Youtube Trailer: https://www.youtube.com/watch?v=X8I-oQymna0

We all deserve to live in a better place, this is what aviato is all about; making the world we live in a better place.

FOR WINDOWS:
1) Run ```pip install -r requirements.txt```
2) Run ```python manage.py runserver```

FOR LINUX/MAC:
1) Run ```pip3 install -r requirements.txt```
2) Run ```python3 manage.py runserver```


## Basic Idea
The basic idea is for the citizens report problems/crimes that they see.



## Post
A Post conists of vital information such as:
1) Title.
2) Description.
3) Image.
4) The municipality in which the problem exists/crime took place.
5) The category of the problem/crime. (Main difference: Natural Disaster/Crime)
6) Location of the problem/crime.
## User
A users necessary information consists of:
1) Username.
2) Email.
3) Password.

He can create/delete/edit his posts read others posts from the dashboard and has a profile page.

## Dashboard
The Dashboard is where all the posts are being displayed to the users.
## Superuser
This belongs to the mayors of the municipalities and can be acceses by typing /admin
Passwords and usernames are given from me to them and a superuser can:

1)Delete Posts
2)Delete Comments

And everything that a normal user can do.
## Blurfaces
This is a feature that blurs faces in the photo taken by the user(if they exist) to deal with GDPR.
## Installation
You need to have Python3.10 installed in your computer.

Go to the directory in which the manage.py file exists.
