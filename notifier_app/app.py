import json
import time
from logging import config, getLogger

from constant import PATH_LOGGING_CFG_FILE, TAGS, TEXT_PATTERNS, URLS
from models.model import search


# Logging
with open(PATH_LOGGING_CFG_FILE, "r") as f:
    log_conf = json.load(f)

config.dictConfig(log_conf)
logger = getLogger(__name__)


# Main
is_found = False
while is_found != True:
    for k in URLS.keys():
        for prod_name, url in URLS[k].items():
            logger.info(f"商品 {prod_name}: {url}")
            found = search(prod_name, url, TAGS[k], TEXT_PATTERNS[k])

            if found == True:
                is_found = True
    time.sleep(60)
