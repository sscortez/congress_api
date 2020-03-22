
import json
import os

import pandas as pd

from connections import get_recently_introduced_bills
from helpers import load_json, set_dataframe_view, ingest_output


OFFSET = 20
SETS = 8


def main(sets=SETS):
    i = 1
    outputs = []
    while i <= sets:
        offset = OFFSET * i
        res = get_recently_introduced_bills(offset=offset)
        outputs.append(ingest_output(res))
        print(f"i: {i}")
        i += 1
    return pd.concat(outputs)


if __name__ == "__main__":
    df = main()