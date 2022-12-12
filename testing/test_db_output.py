# Test cases for Core Banking System project

# @author: WinC Python project Group4
# """
from vardata import *
from send_email import sendEmail

# test output of transaction yearly query with dataframe operations
def test_transaction_yearly(db, df_test):
    query = select_query2.format(table_name)
    transactions = db.execute_SELECT_query(query)
    tst_data = df_test.get_df_data()
    ou = tst_data.groupby([year_col,operation_col]).count().sort_values([transid_col])[[transid_col]].groupby([year_col]).tail(1)
    assert len(transactions) == len(ou)

# test account id selected has balance less than 800
def test_email_account_balance(db):
    query = balance_query
    transactions = db.execute_SELECT_query(query)
    assert len(transactions[transactions['balance'] > 800]) == 0

# test send email functionality
def test_send_email():
    resp = sendEmail('This is a test message sent to wincpyth@gmail.com')
    assert resp == {}


  
    


