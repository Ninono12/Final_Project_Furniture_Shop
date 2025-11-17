Final Project - Furniture Shop

Installation & Setup

Clone the repository:

git clone https://github.com/Ninono12/Final_Project_Furniture_Shop.git
cd Final_Project_Furniture_Shop

Create and activate a virtual environment:
python -m venv venv

venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Project Structure:
catalog/ – models, serializers, views, urls, tasks, tests, apps, admin
config/ - celery, settings, urls, asgi, wsgi
media/ – uploaded media files; 
users/ - admin, apps, models, serializers, tests, urls, views
static/ – #static assets (CSS, JS, images)
templates/ - #
venv/ - #
db.sqlite3 – prefilled with test data

Authentication:
JWT authentication via DRF Simple JWT
API Endpoints
/api/register/ – Register a new user
/api/login/ – Login and obtain JWT tokens

Celery Tasks:
Periodic tasks (e.g., order notifications) are handled via Celery & Redis.
Start the Celery worker:
celery -A Final_Project_Furniture_Shop worker -l info

Start Celery Beat for periodic tasks:
celery -A Final_Project_Furniture_Shop beat -l info

Collect static files:
python manage.py collectstatic

Create additional test data or populate the database:
python manage.py loaddata initial_data.json

Contact

For issues or questions, contact the project author via GitHub: Ninono12


#Notes:
Ensure Redis server is running before starting Celery.
Test data is already included in db.sqlite3.
Media uploads are stored in the media/ folder.
Static files are served from the static/ folder.