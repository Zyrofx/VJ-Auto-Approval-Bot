# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "6573399998:AAHvZbhwRP9aNBPYrBWYEzumkI5mIgiXq6A")
    FSUB = getenv("FSUB", "MvM_Links")
    CHID = int(getenv("CHID", "-1002160712759"))
    SUDO = list(map(int, getenv("SUDO", "1746132193 1353275714").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rangnarl47:reqbotzyro@cluster0.zt0ld.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    PORT = int(getenv("PORT", "8000"))

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
