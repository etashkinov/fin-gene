import os

import quandl
import pickle


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
