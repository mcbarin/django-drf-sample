## Build and Run
```bash
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Navigate to this using browser:
[http://localhost:8000/api/](http://localhost:8000/api/)
