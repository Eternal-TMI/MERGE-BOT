import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "d7877fa235f24635921e287aaa800507")
    BOT_TOKEN = os.environ.get("BOT_TOKEN" , "6716886799:AAFmg-gSpr6qdn63LQmtWhFL3f_xi6yuAQw")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", 6459362)
    OWNER = os.environ.get("OWNER", 1479609725)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Artist_Kun")
    PASSWORD = os.environ.get("PASSWORD","")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("LOGCHANNEL",-100221610400)  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQBQTmWAuk4-qLUiJNnBk0w0bt7jWDvqrolpaqHdaI_vzQY96RTetZ0Sc9H6HCqCnqXRG24vWTMFHH1XzOyvv2bn6jgOLHXoQ6RptA-h6QHQLPnNbW0sU2OeEghDztUm37wF4vVcvCIfMevHw7kO-P6qI5d6U3qFrGtYNdY_TMwrIAWSi2OzkT_HgZqSsq7cYFK8K1y6-C-OqdmwQ04aJGrQ_GfxA1BPi9fOpxB6Qr6106HtEVKFY8SbB5KlP54d4F3pAsbIK3EADfvf34HI-pPU-JjFgCZ2XGSVwLo1gLiprsSegYYwCS_QiASVVRwPBFh4YSsFlnueqs-8QB2elpXuAAAAAVvUBwcA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
