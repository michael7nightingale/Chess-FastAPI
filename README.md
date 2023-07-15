# Fullstack chess game

`FastAPI` RESTFul API backend and `PyQt6` frontend (pure python project, instead of 1 .json file!).
Websockets are the heart of the projects. You may clone this repo twice to play (otherwise you will be recognized as the 
same user instead of two different user, logically).

## Stack:
- FastAPI;
- SQLAlchemy;
- Websockets;
- PyQt6;


## Requirements
Install server requirements:
```commandline
pip install -r server/server-requirements.txt
```

...and client requirements:
```commandline
pip install -r client/client-requirements.txt
```

## Linter
Install development requirements.
```commandline
pip install -r dev-requirements.txt
```
I use `flake8` as Python linter.
```commandline
flake8
```

## Running

### 1st user (with server)
Clone this project to the directory `Chess1`, for example.

Make migrations.
```commandline
cd server
alembic revision --autogenerate
```
Watch the migration id and migrate (ad9al3dss, for example).
```commandline
cd server
alembic uprade ad9al3dss
```

Then run server.
```commandline
cd server
uvicorn main:create_app --port 8001
```

Open other terminal window and run the PyQt application window.
```commandline
cd client
python main.py
```

### 2nd user (with server)
Clone this project to the directory `Chess2`, for example. Then run the PyQt application window.
Open other terminal window and run the PyQt application window.
```commandline
cd client
python main.py
```

## Register your account and enjoy playing~!!
