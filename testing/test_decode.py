# Test cases for Core Banking System project

# @author: WinC Python project Group4
# """
import os
import pandas as pd
import numpy as np
import pytest
from vardata import output_file, input_file, transid_col

# create df_test available entire module for decoded file
@pytest.fixture(scope='module')
def df_test():
    df_test = pd.read_csv(output_file, delimiter='|', low_memory=False)
    yield df_test
    del df_test

# test input file availability
def test_input_file_exists():
    assert os.path.exists (input_file == True)

# test decoded file columns, rows, No of NULL and non-NULL columns
def test_decode_file(df_test):
    row, col = df_test.shape
    assert row == 1056320
    assert col == 16
    assert len(df_test.columns[df_test.isna().any()]) == 4
    assert len(df_test.columns[df_test.notna().all()]) == 12

# test existing values are present in decoded file
def test_dataframe_values(df_test):
    vals = df_test[transid_col].isin(['T00637742','T00171812'])
    flag = 1
    if vals.values.any():
        assert flag >= 1
    else:
        assert flag < 1

# test values are NaN in specified location
def test_dataframe_NaN_values(df_test) :
    assert np.isnan(df_test.iloc[0][7])

# test non-existing values are present in decoded file
@pytest.mark.xfail(reason='Deliberately failed - Values not in Dataframe')
def test_expected_fail():
    vals = df_test[transid_col].isin(['T0001','T0002'])
    flag = 1
    if vals.values.any():
        assert flag >= 1
    else:
        assert flag < 1
   
# test skip functionality
@pytest.mark.skip(reason='Deliberately skipped')
def test_check():
    assert 'hi'

    
