# grief forum 
To anyone who might stumble across this repo:

I built this to create a safe space for individuals mourning the loss of a loved one 
by suicide. Here is the app in its entirety if you want to learn how to build a forum 
and maybe help process your own grief. Remember to always be kind to yourself, especially 
when you are grieving. 

Wishing you the best, 

Joe 

# features 
- create, view, and delete memorial posts
- register, log in, and post using a display name
- post deletion is restricted to authors
- mobile-friendly layout using semantic HTML and CSS
- configurable via `.env` for easy deployment or local testing

## getting started 

1. clone repo 

git clone https://github.com/yourusername/grief-forum.git
cd grief-forum

2. create and activate venv 

python3 -m venv venv
source venv/bin/activate

3. install dependencies 

pip install -r requirements.txt

4. environment variables 

cp .env.example .env

5. db migrations 

python manage.py migrate

6. run dev server

python manage.py runserver

## config 

environment variables managed via python-decouple and a .env file

DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
DATABASE_URL
Optional email backend settings (SMTP)

## project structure

grief_forum/
├── forum/              # Main Django app
├── forum_project/      # Project config
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS)
├── db.sqlite3          # SQLite database (local only)
├── .env.example        # Environment variable template
└── README.md           # You're reading it!

## .env example 
Here's what your .env file should look like:

DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=sqlite:///db.sqlite3

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=your-email@example.com

## licensing 
project is licensed under the MIT License: https://opensource.org/licenses/MIT 

## contributing
- open to contributions that align with its mission of mental health support
- if you’d like to suggest a feature or fix a bug, feel free to open an issue or submit a 
  pull request

## acknowledgements
this project was built with Django and inspired by the desire to create a gentle space for grief expression and healing