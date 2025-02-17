from os import environ

API_ID = int(environ.get("API_ID", "15657755"))
API_HASH = environ.get("API_HASH", "7cce51d4664d010b90ad690e0d5121ad")
BOT_TOKEN = environ.get("BOT_TOKEN", "7925953890:AAFT6mnQPK3E1yqKf3Sr9-GwWdhnevSWx7Y")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002440769217"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002351435664"))
ADMINS = int(environ.get("ADMINS", "5003133371 6650849235"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://Tgbot:123@cluster0.bz1f9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0/")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
