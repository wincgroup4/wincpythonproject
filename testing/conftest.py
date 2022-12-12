import pytest
from utilities import DataframeUtility
from vardata import *
from db_utilities import SqlRepo

# Add custom report title for pytest report
def pytest_html_report_title(report):
    ''' modifying the title  of html report'''
    report.title = "Pytest report for Core Banking System Project"

# This is for Dataframe object and available for all testcases
@pytest.fixture(scope='session')
def df_test():
    df_test = DataframeUtility('test_df', output_file)
    df_test.drop_null_cols()
    yield df_test
    del df_test

# This is for Database object and is available for all testcases
@pytest.fixture(scope='session')
def db(df_test):
    df_db = df_test.get_df_data(table_columns)
    db = SqlRepo(db_name, df_db)
    yield db
    del db