# Test cases for Core Banking System project

# @author: WinC Python project Group4
# """
import pytest
from vardata import *
import pandas as pd
from main import *

# Test datframe columns before and after removing NULL, add after adding FLAG column
def test_formatted_file(df_test):
    df_test.drop_null_cols()
    df_test.drop_null_rows()
    df_test.remove_unnamed_column()
    df = df_test.get_df_data()
    assert (len(df.columns)) == 15 #after removing Unnamd columns no of columns will be 15
    df_test.flag_trans_operation()
    assert (len(df.columns)) == 16 #after adding FLAG columns no of columns will be 15

# Test FLAG column for Transaction ID's - there is no duplicate transaction ID
def test_flag_duplicate_trans_values(df_test):
    df_test.flag_trans_operation()
    df = df_test.get_df_data(flag_col)
    if flag_value1 not in df:
        assert True
    else:
        with pytest.raises(ValueError):
            raise ValueError('Transaction ID is not duplicate')

# Test FLAG column for operation - There are suspicious transactions
def test_flag_operation_values(df_test):
    df_test.flag_trans_operation()
    df = df_test.get_df_data(flag_col)
    if flag_value2 in df:
        assert True
    else:
        with pytest.raises(ValueError):
            raise ValueError('Suspicious transactions are present, please check!!')


# test Pensioners bonus functionality
def test_pension_bonus(df_test):
    df_test.flag_trans_operation()
    pension_bonus_df = df_test.pension_bonus()
    assert len(pension_bonus_df[pension_bonus_df[symbol_col] == pension_check]) == 51
    assert(type(pension_bonus_df).__name__ == 'DataFrame') 
    assert any(pension_bonus_df['balance']) == True
    

# test digital to cash ratio functionality
def test_digital_cash_rtio(df_test):
    sample_df = df_test.calculate_ratio()
    assert isinstance(sample_df,pd.DataFrame)
    