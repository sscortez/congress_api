
import json
import os

import requests


BASE_URL = "https://api.propublica.org/congress/v1"
CONGRESS = "116"
CHAMBER = "both"

_dirname = os.path.dirname(__file__)


def get_token():
    jfile = os.path.join(_dirname, 'token.json')
    with open(jfile) as f:
        f = f.read()
        data = json.loads(f)
    return data


def get_recently_introduced_bills():
    headers = get_token()
    api_request = "/".join([BASE_URL, CONGRESS, CHAMBER, "bills/introduced.json"])
    return requests.get(api_request, headers=headers)