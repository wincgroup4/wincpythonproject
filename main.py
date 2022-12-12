# main program for Core Banking System project
# '''
# @author: WinC Python project Group4
# """

from send_email import sendEmail
from utilities import *
from db_utilities import *
from plot_graph import draw_chart

# Function to get formatted Dataframe
def get_formatted_df_req1():
    global df_obj
    df_obj = DataframeUtility('bank_df', output_file)   # Instantiate utility class object
    df_obj.drop_null_cols()
    df_obj.drop_null_rows()
    df_obj.remove_unnamed_column()
    df_obj.flag_trans_operation()
    logging.info('Dropped all NULL rows and cols and FLAG column created')
    df_obj.log_dataframe()

# Function to get most transations done in a year
def get_transaction_by_year_req2_1():
    global df_db
    global repo
    df_db = df_obj.get_df_data(table_columns)
    repo = SqlRepo(db_name, df_db)              # Instantiate db utility class object
    repo.create_and_load_table(table_name)
    query = select_query2.format(table_name)
    transactions = repo.execute_SELECT_query(query)
    transactions.to_csv(transaction_output_file, header=transaction_output_headers, index=False)
    logging.info('Output file '+ transaction_output_file + ' created successfully')

# Function to send emails to accounts whose balance is < 800
def send_email_req2_2():
    query = balance_query
    trans_df = repo.execute_SELECT_query(query)
    trans_df.to_csv('output_files\\acc.csv', index=False)
    for i in range(len(trans_df.head(5))):
        acc = trans_df.loc[i, accid_col]
        bal = trans_df.loc[i, bal_col]
        msg = mail_body.format(acc, bal)
        # print(msg)
        sendEmail(msg)

# Function to create 10 users monthwise with most transactions
def create_top_10_user():
    query = top_users_query
    transactions = repo.execute_SELECT_query(query)
    transactions.to_csv(top_10_users, index=False)

# Function to create old pensioners file 
def create_old_pensioners_req3_1():
    pension_df = df_obj.pension_bonus()
    pension_df.to_csv(bonus_file, index=False)
    logging.info(bonus_file + ' created successfully')

# Function to find max Digital-Cash ratio institute and plot a graph for the same
def calculate_ratio_req3_2():
    ratio_df = df_obj.calculate_ratio()
    draw_chart(ratio_df,chart_file)
    logging.info('digital-to-cash transactions plotted in graph, refer file:' + chart_file)


# begin = time.time()
# logging.info('--------------Execution started---------------')
# # decode_file(input_file , output_file)
# get_formatted_df_req1()
# get_transaction_by_year_req2_1()
# send_email_req2_2()
# # create_old_pensioners_req3_1()
# # calculate_ratio_req3_2()
# logging.info('--------------Execution completed---------------')

# # retcode = pytest.main(["-x", "testing"])
# # pytest.main(["-x", "testing"])

# end = time.time()
# print(f"Total runtime of the program is {end - begin}")