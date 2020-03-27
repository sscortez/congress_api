
import os
import json
from collections import OrderedDict

import pandas as pd


_dirname = os.path.dirname(__file__)


def set_dataframe_view():
    pd.set_option('display.width', 180)
    pd.set_option('display.max_columns', 50)
    pd.set_option('display.max_colwidth', 60)
    return True


def load_json(filename, object_pairs_hook=None):
    if '.json' not in filename:
        filename += '.json'
    jfile = os.path.join(_dirname, filename)

    with open(jfile) as f:
        f = f.read()
        file_output = json.loads(f, object_pairs_hook=object_pairs_hook)
    return file_output


def ingest_output(result):
    data = json.loads(result.content)
    data = data['results'][0]['bills']
    col_data = load_json('storage', OrderedDict)['relevant_columns']
    cols = [x for x in col_data]
    _df = pd.DataFrame(data)[cols]
    for k, v in col_data.items():
        if v in ['string', 'int', 'boolean']:
            _df[k] = _df[k].astype(v)
        elif v == 'date':
            _df[k] = pd.to_datetime(_df[k]).dt.date
        else:
            pass
    return _df
