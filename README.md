# Global Bites API

## Development environment Setup
Clone project and change directory to project folder

```
git clone https://github.com/joshua-mjjj/twelve_oaks_test_backend.git
```

Create a virtual env with 
```
python -m venv env or python3 -m venv env
```

Activate virtual env
```
cd env && /source/bin/activate
```

Install requirements inside virtual env
```
pip install -r requirements.txt
```

Go back to project root
```
cd ..  
```

Run project 
```
python manage.py runserver  
```

Running Tests. 
Unit Test 1: Get restaurants data
Unit Test 2: Get restaurant detail data

Run Tests 
```
python manage.py test
```