### Final Project - Furniture Shop

## Installation & Setup

### Clone the repository:
git clone https://github.com/Ninono12/Final_Project_Furniture_Shop.git
cd Final_Project_Furniture_Shop

### Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  

### Install dependencies:
pip install -r requirements.txt

### Apply migrations:
python manage.py migrate

### Create a superuser:
python manage.py createsuperuser

### Run the development server:
python manage.py runserver

## Project Structure
catalog/ – models, serializers, views, urls, tasks, tests, apps, admin  
config/ – celery, settings, urls, asgi, wsgi  
media/ – uploaded media files  
users/ – admin, apps, models, serializers, tests, urls, views  
static/ – style.css (minimal static file for structure)  
templates/ – products.html (minimal template for structure)  
venv/ – virtual environment files (include, lib, scripts)  
db.sqlite3 – prefilled with test data

**Note:** Frontend is minimal; templates and static folders exist for project structure only.

## Authentication
JWT authentication via DRF Simple JWT

## API Endpoints:
POST /api/register/ – Register a new user
POST /api/login/ – Login and obtain JWT
GET /api/cart/ – View cart
POST /api/cart/add/ – Add product to cart
POST /api/cart/remove/ – Remove product from cart
GET /api/orders/ – List of my orders
GET /api/orders/<id>/ – Order details
POST /api/orders/create/ – Create a new order


## Celery Tasks
Periodic tasks (e.g., order notifications) are handled via Celery & Redis.

### Start the Celery worker:
celery -A Final_Project_Furniture_Shop worker -l info

### Start Celery Beat for periodic tasks:
celery -A Final_Project_Furniture_Shop beat -l info

## Static & Media Files
Media uploads are stored in the media/ folder  
Static files are served from the static/ folder

### Collect static files:
python manage.py collectstatic

## Test Data
Test data is already included in db.sqlite3.  
To create additional test data or populate the database:  
python manage.py loaddata initial_data.json

## Contact
For issues or questions, contact the project author via GitHub: Ninono12

## Notes
- Ensure Redis server is running before starting Celery.  
- Front-End (templates & CSS) is minimal and emplates and static folders exist for project structure only.  
- Test data is preloaded in db.sqlite3.  
- Media uploads are stored in the media/ folder.

