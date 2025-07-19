# config.py

import logging
from decouple import config

# Setup logger
LOGS = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = int(config("DEV"))
    OWNER = config("OWNER").split()
    
    # Optional configs
    THUMB = config("THUMBNAIL", default="thumb.jpg")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By AnshuSharma (https://github.com/Anshusharma75/TG-videoCompress)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]

except Exception as e:
    LOGS.error("❌ Environment vars Missing or Invalid!")
    LOGS.error(str(e))
    exit(1)
