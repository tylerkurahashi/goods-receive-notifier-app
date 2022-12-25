import json
import os
import sys
from logging import config, getLogger
from typing import Dict

import requests
from box import Box # type: ignore
from bs4 import BeautifulSoup


"""
Model code
"""
if __name__ == "__main__":
    sys.path.append("/workspace")

from constant import PATH_LOGGING_CFG_FILE, SLACK_NOTIFICATION_URL, SLACK_USER_ID, TAGS, TEXT_PATTERNS, URLS


URLS = Box(URLS)
TAGS = Box(TAGS)
TEXT_PATTERNS = Box(TEXT_PATTERNS)

"""
CONFIG
"""
PATH_THIS_LOGGING_CFG = os.path.join(os.path.dirname(__file__), "..", PATH_LOGGING_CFG_FILE)
with open(PATH_THIS_LOGGING_CFG, "r") as f:
    log_conf = json.load(f)

config.dictConfig(log_conf)
logger = getLogger(__name__)

logger.info(f"main run -->> this file: {__file__}")


def notify(prod_name: str, url: str) -> None:
    """
    send notification to workspace when storage is not empty
    """

    json_data = {"text": f"<@{SLACK_USER_ID}>\n{prod_name}入荷!もしくは予約空いとる!\n{url}"}

    requests.post(SLACK_NOTIFICATION_URL, data=json.dumps(json_data))


def search(prod_name: str, url: str, tags: Dict, text_pattern: str) -> bool:
    """
    search url and find if goods are stored
    """
    logger.debug(f"url:{url}")
    logger.debug(f"tags:{tags}")
    logger.debug(f"text_pattern:{text_pattern}")

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find_all(**tags)
    logger.debug(f"result:{result[0].text.strip()}")

    if result[0].text.strip() != text_pattern:
        logger.info(f"{prod_name}入荷!もしくは予約空いとる!")
        notify(prod_name, url)
        return True
    else:
        logger.info("まだあかんなぁ")
        return False


if __name__ == "__main__":
    for k in URLS.keys():
        for prod_name, url in URLS[k].items():
            logger.debug(f"商品 {prod_name}: {url}")
            search(prod_name, url, TAGS[k], TEXT_PATTERNS[k])
            break
