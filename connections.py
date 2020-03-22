
import json
import os

import requests

from helpers import set_dataframe_view, load_json

BASE_URL = "https://api.propublica.org/congress/v1"


def get_recently_introduced_bills(congress="116", chamber="both", offset=20):
    headers = load_json('token')
    _offset = f"?offset={offset}"
    api_request = "/".join([BASE_URL, congress, chamber, "bills/introduced.json", _offset])
    return requests.get(api_request, headers=headers)
