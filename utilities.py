# '''
#     This module contains functional utilities for formating dataframe
#     Below are the functions:
#     1. decode_file - Decodes the input file and creates decoded output file
#     2. catch_exception - Function is a decorator used to catch any exceptions 
#     3. Logs the executed step information to 'tmp.log'

#     CLASS DataframeUtility defines all major dataframe operations
# '''
# @author: WinC Python project Group4
# """

import functools
import logging
import pandas as pd
import numpy as np
import uu
from vardata import *

# logging configuration
logging.basicConfig(filename='tmp.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level='DEBUG')

# Decorator for Exception handling
def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logging.error('Caught an exception in function:' + str(f.__name__) + ' -----> ' + str(repr(e)) )
    return func

# Function to decode the encoded file
@catch_exception
def decode_file(infile , outfile):
    uu.decode(infile,outfile)
    logging.info('Input file: ' + infile + ' decoded successfully')
    return outfile

# Class for handling dataframe operations
class DataframeUtility:
    @catch_exception
    def __init__(self, df_name, outfile):
        self.df = df_name
        self.df = pd.read_csv(outfile, sep = '|', low_memory = False)
        logging.info('Instantiated the object')

    # Function to drop null values in columns
    def drop_null_cols(self):
        self.df.dropna(axis=1, how='all')
        logging.info('Dropped all NULL columns in the dataframe')

    # Function to drop null values in rows
    def drop_null_rows(self):
        self.df.dropna(axis=0, how='all', inplace= True)
        logging.info('Dropped all NULL rows in the dataframe')

    # Function to remove unnamed column in Dataframe
    def remove_unnamed_column(self):
        self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]

    # lambda function to append values to column
    def add_flag_value(self, val):
        f = lambda x: val if x == '' else x + ',' + val
        return f
    
    # Function to add FLAG column to Dataframe
    def flag_trans_operation(self):
        duplicates = pd.Series(np.where((self.df[transid_col].duplicated(keep=False)), flag_value1, ''))
        suspicious = pd.Series(np.where((self.df[operation_col].isnull()), flag_value2,''))
        self.df[flag_col] = np.where(duplicates == '', suspicious, 
                            np.where(suspicious == '', duplicates,
                            duplicates + ',' + suspicious))
        logging.info('FLAG column updated with:' + flag_value1 + 'and ' + flag_value2)

    # Function to return dataframe with specified columns
    def get_df_data(self,cols=None):
        if cols == None:
            return self.df
        else:
            return self.df[cols]
     
    def display_df_col(self, col):
        print(self.df[col].head(10))

    # Function to return dataframe with added value to FLAG column for pensioners bonus for Bank of America
    def pension_bonus(self):
        pension_df = self.df.loc[(self.df[bank_col] == bank_check) & (self.df[bal_col] > 0) &
                                (self.df[symbol_col] == pension_check)].copy()
        pension_df.sort_values(by=[accid_col, date_col], inplace=True)
        pension_df.drop_duplicates(subset=[accid_col], keep='last', inplace=True)
        f = lambda x: round(x+(x*0.05),3)
        pension_df[bal_col] = pension_df[bal_col].apply(f)
        pension_df[flag_col] = pension_df[flag_col].apply(self.add_flag_value(flag_value3))
        return pension_df
        # update dataframe with latest values
        # self.df = self.df.set_index([transid_col])
        # pension_df = pension_df.set_index([transid_col])
        # self.df.update(pension_df)
        # self.df = self.df.reset_index()

    # Function to calculate Digital over Cash ratio and returns Dataframe
    def calculate_ratio(self):
            self.df[new_trans_col]=self.df[operation_col].map(check_cash)
            self.df[[bank_col]] = self.df.groupby(accid_col)[[bank_col]].ffill().bfill()
            sub_df = self.df[['bank','op']]
            ratio_df = pd.pivot_table(sub_df, index=bank_col, columns=new_trans_col, aggfunc=len, fill_value=0)
            ratio_df = ratio_df.reset_index()
            ratio_df[ratio_col] =(ratio_df['DIGITAL'] / ratio_df['CASH']).apply(lambda x: float("{:.3f}".format(x)))
            logging.info('Highst Digital/Cash transaction financial instituton is:\n' +  str(ratio_df[ratio_df.ratio == ratio_df.ratio.max()]))
            return ratio_df
            
    def log_dataframe(self):
        logging.info('No. of rows and columns in Dataframe::' + str(self.df.shape))
        logging.info('No. of columns containing null values:' + str(len(self.df.columns[self.df.isna().any()])))
        logging.info('No. of columns not containing null values:' + str(len(self.df.columns[self.df.notna().all()])))
        logging.info('Total no. of columns in the dataframe' + str(len(self.df.columns)))

# Function to map map values to operation fields 
def check_cash(val):
    if val == 'Credit in Cash':
        trans = 'CASH'
    elif val == 'Cash Withdrawal':
        trans = 'CASH'
    elif val == 'Credit Card Withdrawal':
        trans = 'CASH'
    elif val == 'Remittance to Another Bank':
        trans = 'DIGITAL'
    elif val == 'Collection from Another Bank':
        trans = 'DIGITAL'
    else:
        trans = 'INVALID'
    
    return trans
