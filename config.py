import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5651484775").split()))
OWNER_ID = int(getenv("OWNER_ID", "5651484775"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://bara:jiwa@cluster0.phhun7f.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5700306396:AAEEW3h3YDg336WA62hTehaDAF9Ij7Exb4I")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAQCFb7H_5-rWPE9aDZjrpkpS7FitrfLLtgrJzR6sspkKnFVwJuzcCb9V9CBWgiMII7ug_yp1qEffxrImxowpy6jU3VpFCoX-YtMX8d8Y-iabIyJQaCkJ9ptqG4AJSZjen81KZnbEm84WhcKwRM8ezr5eVnXFv1gcJJrmlkqhQaCjeSY4sojLs0PfSL_SreLBasDbKCVD9Po9eHHvl9TggpHoR8EGeomLTc8MGan6YsXpQNvNpwZH1kX3_xGy_khXYRGYjDvW-uKKU8GVh8iHUXHRJPbTLlnopGQmEngGfPzbO1_ITVYsdZaZx6o3jJnda9qQcgjcn6rFh693V8tlsxAAAAAFQ2tBnAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
