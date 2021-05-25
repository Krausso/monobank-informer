#!/bin/bash
TOKEN=""

read -p "Telegram bot API token: " TOKEN

sudo apt install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

echo "
[production]
TOKEN = $TOKEN
" > app/.secrets.toml
