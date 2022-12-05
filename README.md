[bookmarks-login](https://web-production-9da7.up.railway.app/account/login)
[register](https://web-production-9da7.up.railway.app/register)
[edit](https://web-production-9da7.up.railway.app/edit)
[dashboard](https://web-production-9da7.up.railway.app/account)
# Functionality: What the app can do?
 <p> I learned how to build an authentication system for my site. I implemented all 
the necessary views for users to register, log in, log out, edit their password, and reset their password. 
I built a model for custom user profiles, and I created a custom authentication backend to let 
users log into my site using their email address.</p>
<p>
    I added social authentication to my site so that users can use their existing Facebook, Twitter, Github, LinkedIn or Google accounts to log in. I used Python Social Auth and implemented social authentication using OAuth 2.0, the industry-standard protocol for authorization. I also learned how 
    to serve my development server through HTTPS using Django Extensions. Finally, I customized 
    the authentication pipeline to create user profiles for new users automatically.
</p>

## Basic commands
- pipenv install Django~=4.1.0
- python manage.py createsuperuser
- pipenv install Pillow==9.2.0
- pipenv install social-auth-app-django
- pipenv install django-extensions
- pipenv install werkzeug==2.2.2
- pipenv install pyOpenSSL==22.0.0
- python manage.py runserver_plus --cert-file cert.crt
- pipenv install gunicorn
- pip freeze > requirements.txt
- python --version
- python manage.py collectstatic
- pipenv install python-dotenv
- pipenv install whitenoise