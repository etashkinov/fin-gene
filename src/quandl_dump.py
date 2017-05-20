import os

import quandl
import pickle

import pandas as pd
import time

from storage import Storage


def __get_file_name(name):
    return "resources/" + name.lower().replace(r"/", "-") + ".pickle"


def __dump_stock(df, file_name):
    with open(file_name, "wb") as f:
        pickle.dump(df, f)


def __load_stock(file_name):
    with open(file_name, "rb") as f:
        return pickle.load(f)


def get(name):
    file_name = __get_file_name(name)
    if os.path.exists(file_name):
        return __load_stock(file_name)
    else:
        df = quandl.get(name)
        __dump_stock(df, file_name)
        return df


def get_list(exchange_name):
    with open("resources/" + exchange_name + ".csv", "r") as f:
        companies_list = pd.read_csv(f)
        return companies_list['Symbol']


def get_stored():
    storage = Storage()
    stored = storage.get_all()
    return [(c['symbol'], pickle.loads(c['df'])) for c in stored]


def dump(company_symbols):
    storage = Storage()
    try:
        do_dump(company_symbols, storage)
    except quandl.QuandlError as e:
        if e.http_status == 429:
            print(e)
            print("Wait for 600 seconds")
            time.sleep(600)
            dump(company_symbols)
        else:
            raise


def do_dump(company_symbols, storage):
    symbol = storage.get_latest_symbol()
    print("Latest symbol:", symbol)
    for s in sorted(company_symbols):
        if not symbol or s > symbol:
            print("Query for:", s)
            quandl_key = "WIKI/" + s
            try:
                df = pickle.dumps(quandl.get(quandl_key))
                result = 'success'
            except quandl.QuandlError as e:
                if e.http_status == 404:
                    df = None
                    print("Failed to load ", s, ":", e)
                    result = 'fail: ' + str(e)
                else:
                    raise

            storage.insert_data(s, "quandl", quandl_key, df, result)
            print(s, "stored")

