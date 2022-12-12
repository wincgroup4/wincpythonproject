'''# Test cases for Core Banking System project

# @author: WinC Python project Group4
# """
import os
import pytest
from vardata import *

f = "..\\"
file_list = [ f+transaction_output_file, f+output_file, f+bonus_file, f+chart_file, 'tmp.log' ]

# test output file exists or not
@pytest.mark.parametrize("file", file_list)
def test_input_file_exists(file):
    assert os.path.exists (file == True)



'''