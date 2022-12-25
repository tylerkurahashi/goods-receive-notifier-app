PATH_LOGGING_CFG_FILE = "logging.json"

URLS = {
    "SHIROGANE": {
        "Keyball39": "https://shirogane-lab.com/products/keyball39",
        "Keyball44": "https://shirogane-lab.com/products/keyball44",
        "Keyball61": "https://shirogane-lab.com/products/keyball61",
    },
    "YUSYAKOUBOU": {
        "Keyball39": "https://shop.yushakobo.jp/products/5357",
        "Keyball61": "https://shop.yushakobo.jp/products/5358",
    },
}

TAGS = {
    "SHIROGANE": {"name": "span", "class_": "badge price__badge-sold-out color-inverse"},
    "YUSYAKOUBOU": {"name": "button", "class_": "product-form__add-button button button--disabled"},
}

TEXT_PATTERNS = {"SHIROGANE": "売り切れ", "YUSYAKOUBOU": "完売"}

SLACK_NOTIFICATION_URL = ""
SLACK_USER_ID = ""
