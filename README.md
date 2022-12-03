# Functionality: What the app can do?
 <p> I learned how to build an authentication system for my site. I implemented all 
the necessary views for users to register, log in, log out, edit their password, and reset their password. 
I built a model for custom user profiles, and I created a custom authentication backend to let 
users log into my site using their email address.</p>

## Basic commands
- pipenv install Django~=4.1.0
- python manage.py createsuperuser
- pipenv install Pillow==9.2.0
- pipenv install social-auth-app-django
- pipenv install django-extensions
- pipenv install werkzeug==2.2.2
- pipenv install pyOpenSSL==22.0.0
- python manage.py runserver_plus --cert-file cert.crt