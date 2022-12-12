#    Variables for all modules
# '''
# @author: WinC Python project Group4
# """
from datetime import timedelta
from datetime import datetime

# [input_output_file]
input_file = 'input_files\\transaction_data_encoded'
output_file = 'output_files\\tranaction_data_decoded_final.csv'
transaction_output_file = 'output_files\\transactions_yearly.csv'
transaction_output_headers = ['Year','No of Transactions','Preferred transaction type']
bonus_file = 'output_files\\bonus_to_pensioners.csv'
chart_file = 'static\\digital-to-cash_stats.html'
top_10_users = 'output_files\\top_10_users_of_month.csv'

# [database]
db_name = 'banking.db'
table_name = 'banking_data'
table_columns = ['trans_id','account_id','type','operation','amount','balance','bank','account','year','month','fulldatewithtime']
# select_query = 'SELECT year, COUNT(operation), operation FROM {} GROUP BY year, operation'
select_query2 = 'SELECT year,MAX(tot) ,operation FROM ( SELECT year, COUNT(operation) as tot, operation from {} GROUP BY year, operation) GROUP BY year'
# select_query3 = 'SELECT account_id, ?balance, bank, max(fulldatewithtime) FROM {} WHERE balance < 800 GROUP BY account_id,bank' 
balance_query = 'SELECT account_id, balance, bank, year FROM ' + table_name + ' WHERE ' \
                'balance BETWEEN 0 AND 799 AND year=(SELECT MAX(year) FROM ' + table_name + \
                ') GROUP BY account_id '
top_users_query = 'SELECT * FROM (SELECT account_id, COUNT(operation) AS transactions, month, row_number() over (partition by ' \
                  'month order by COUNT(operation) desc) as user_rank FROM ' + table_name + ' GROUP BY account_id) ' \
                                                                                                'users WHERE user_rank<=10 '


# [variables]
flag_value1 = 'Transaction ID is duplicate'
flag_value2 = 'Suspicious Transaction'
flag_value3 = 'Pensioner-Bonus Interest Credited'
# [Email]
smtp_domain = "smtp.gmail.com"
smtp_port = 587
mail_from_addr = "wincpythonprojectgroup4@gmail.com"
mail_app_password = 'daqdhvdlbfljewfe'
mail_to_addr = "wincpyth@gmail.com"
due_date_cal = datetime.now() + timedelta(days=10)
due_date = due_date_cal.date()
mail_subject = "Insufficient Bank Balance"
mail_body = "Dear {},\n\t\tYour current balance is {}. As per the bank policy, Customers " \
            "need to maintain an average minimum monthly balance of Rs 800 to keep their savings bank account active. " \
            "\nPlease make sure you maintain the minimum balance in your account by " + str(due_date) + " or might face a penalty" \
            "\n \nThanks"


# [Dataframe columns]
transid_col = 'trans_id' 
accid_col = 'account_id' 
type_col = 'type'
operation_col = 'operation'
amount_col = 'amount'
bal_col = 'balance'
symbol_col = 'k_symbol'
bank_col = 'bank'
account_col = 'account'
year_col = 'year'
month_col = 'month'
day_col = 'day'
fulldate_col = 'fulldate'
fulltime_col = 'fulltime'
date_col = 'fulldatewithtime'
flag_col = 'FLAG'
bonus_col = 'BONUS'
new_trans_col = 'op'
ratio_col = 'ratio'

bank_check = 'Bank of America'
pension_check = 'Old Age Pension'
