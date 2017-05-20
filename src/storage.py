import pymongo


class Storage:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.fin_gene
        self.companies = self.db.companies
        self.companies.create_index([('symbol', pymongo.DESCENDING)], unique=True)

    def get(self, company_symbol):
        return self.companies.find_one({"symbol": company_symbol})

    def get_all(self):
        return self.companies.find({"result": "success"})

    def insert_data(self, company_symbol, source, key, df, result):
        company = {"symbol": company_symbol,
                   "source": source,
                   "key": key,
                   "df": df,
                   "result": result}
        self.companies.insert_one(company)

    def get_latest_symbol(self):
        for i in self.companies.find().sort([('symbol', pymongo.DESCENDING)]).limit(1):
            return i['symbol']

        return None
