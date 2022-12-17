import os

class Config:

    BOT_TOKEN = os.environ["5864233502:AAGHSRL_yespt99VpR1A9AIOwZwoZ-CFP3g"]                                 # Get From https://t.me/BotFather

    API_ID = int(os.environ["16494736"])                                  # Get from https://my.telegram.org/apps

    API_HASH = os.environ["2cb7fa5859e2de684e3e10d9c049621a"]                                   # Get from https://my.telegram.org/apps

    CLIENT_ID = os.environ["260176737372-iu17pd3mkkm4lejrlaatbr08kmo604ec.apps.googleusercontent.com"]                                 # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.environ["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"]                         # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.environ["5071104456"])                            # Bot owner's telegram id You can get with rose or marie

    AUTH_USERS = [BOT_OWNER,5071104456]+[int(user) for user in os.environ["AUTH_USERS"].split(",") if os.environ["AUTH_USERS"]]
                                                                        # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                        # Credentials file



