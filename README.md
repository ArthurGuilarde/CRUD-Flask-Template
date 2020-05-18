## How to run this project

First install all dependencies from "requirements.txt" file.

```Command
pip install -r requirements.txt
```

Second you need set flask configuration

- Unix OS

```Unix
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

- Windowns OS

```Windowns
set FLASK_APP=app
set FLASK_ENV=Development
set FLASK_DEBUG=True
```

Commands to run flask

```
flask run -> Run Flask App

flask db init -> Initialize migrations folder
flask db migrate -> Create migrations based on models
flask db upgrade -> Run migrations
flask db downgrade -> Revert migrations
```
