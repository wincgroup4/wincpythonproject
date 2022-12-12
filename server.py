# FLASK server functions 
# '''
# @author: WinC Python project Group4
# """

from flask import Flask, render_template, Response
import time
import pytest
from main import *

app = Flask(__name__)

# Localhost 
@app.route('/')
def index():
	return render_template('index.html', isIndex = True)

# API for form action
@app.route('/app_run',methods=['POST','GET'])
def get_df():
    resp = []
    begin = time.time()
    decode_file(input_file , output_file)
    pytest.main(["-x", "testing"])
    resp.append('pytest report available')
    resp.append('File decoded successfully')
    get_formatted_df_req1()
    resp.append('Dataframe formatted and removed all NULL columns, all NULL rows added FLAG column')
    get_transaction_by_year_req2_1()
    resp.append('Transaction yearly file created ')
    send_email_req2_2()
    resp.append('Email sent to accounts whose Balance is < 800 ')
    create_top_10_user()
    resp.append('Top 10 users with the most transaction of the month file created')
    create_old_pensioners_req3_1()
    resp.append('Bonus credited to old pension account of Bank of America')
    calculate_ratio_req3_2()
    resp.append('Digital/Cash Transaction')
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")

    return render_template('index.html', resp = resp)

# send Digital to cash Stats page to client
@app.route('/digital-to-cash-stats.html')
def digi():
    return app.send_static_file('digital-to-cash_stats.html')

# send pytest report page to client
@app.route('/pytest-report.html')
def pytest_report():
    return app.send_static_file('pytest_report.html')

# send code covergage report page to client
@app.route('/code-coverage-report.html')
def coverage_report():
    return app.send_static_file('htmlcov/index.html')

# progress bar send data
@app.route('/progress')
def progress():
	def generate():
		x = 0
		while x <= 100:
			yield "data:" + str(x) + "\n\n"
			x = x + 10
			time.sleep(5)

	return Response(generate(), mimetype= 'text/event-stream')


if __name__ == "__main__":
	app.run(debug=True)