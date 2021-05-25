# Installation guide
### Install for development
```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Install using Docker
```shell
docker-compose up -d
```

### Install on your server
Run `install.sh` and input variables (details below):

| VARIABLES                 | DESCRIPTION                                        |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `your_env`                | Project environment. Change in `app/config.py`. Development by default.
| `TOKEN`                   | Telegram bot token from t.me/BotFather.

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