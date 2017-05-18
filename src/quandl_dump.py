import quandl
import pickle


def get_file_name(name):
    return "resources/" + name.lower().replace(r"/", "-") + ".pickle"


def dump_stock(name):
    df = quandl.get(name)
    with open(get_file_name(name), "wb") as f:
        pickle.dump(df, f)


def load_stock(name):
    with open(get_file_name(name), "rb") as f:
        return pickle.load(f)
