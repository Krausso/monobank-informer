# Project setup
```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Run project
```shell
python3 -m app
```

# Manage migrations
```shell
# init alembic
alembic init alembic

# create migration
alembic revision --autogenerate -m "message"

# apply migration
alembic upgrade head

# downgrade migration
alembic downgrade base
```