
import sqlite3
from utilities import catch_exception,logging,pd

class SqlRepo:
    @catch_exception
    def __init__(self, db_name, df):
        self.df = df
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        logging.info('Connection to Database ' + db_name + ' established')

    @catch_exception
    def create_and_load_table(self, table_name):
        self.df.to_sql(table_name, self.conn, if_exists = 'replace', index = False)
        logging.info('Table ' + table_name + ' created and loaded with dataframe data')

    @catch_exception
    def execute_SELECT_query(self, query):
        transactions = pd.read_sql(query, self.conn)
        logging.info('select query :: ' + query + ' executed')
        return transactions

        





