import os

API_ID = API_ID =  27862677

API_HASH = os.environ.get("API_HASH", "e343ce2c81b2b6c2c0d6bee58284e3bd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7063024370:AAFHuTYE6bOwjI5s3Nodv2mi8JGctq15nu0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5881684718))

LOG = -1002182529805,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [5219193259,1327415906]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5881684718").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


