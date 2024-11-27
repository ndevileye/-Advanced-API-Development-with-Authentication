Setup Instructions

1)Clone the repository:
git clone <repository-url>
cd <repository-folder>

2)Set up a virtual environment:
python3 -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

3)Install the dependencies:
pip install -r requirements.txt

4)Add additional configurations to the .env file:

EMAIL_HOST=<SMTP server>
EMAIL_PORT=<SMTP port>
EMAIL_HOST_USER=<Your email>
EMAIL_HOST_PASSWORD=<Your password>

5)Apply migrations:
python manage.py migrate

6)Create a superuser:
python manage.py createsuperuser

7)Start the server:
python manage.py runserver

8)Start the reds
redis-server

9)Run the Celery worker
celery -A celery worker --loglevel=info


The API JSON file is included in the folder for testing.