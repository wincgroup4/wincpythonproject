# wincpythonproject
Core Banking System

This project is to perform the various banking operations such as decoding the encrypted data file, validating the data, getting trascation data and ratio, 
adding bonus based on customer details, getting ratio of transcations, sending mails as an alert for in-sufficient balance and getting top 10 users for each
month.

#Decoding:
decoding is done using the uu library which generates the output.csv file with the decoded data.

#Validating Data:
the data validation is performed by checking for null rows and columns and removing the same using dataframe and pandas libraries. We also remove any un-named
columns as well.

#Flagging:
we add a new column 'Flag' to identify the different scenarios like ->
'Suspicious transaction' for the rows for which the operation column is empty or null.
'Transaction ID is duplicate!' for rows with duplicate transaction id. 
'Pensioner-Bonus Interest Credited' for rows with bank as 'Bank of America' and k_symbols as 'Old Pensioner'.

#Yearly transaction:
we get the total transcations made in each year and the type of transaction that was the highest and generate the trasaction.csv file with these details.
for this we have added our data to a table in DB using sqlite3.

#Sending Mail:
we use the SMTP server and a google account to send and receive the mails for rows having balance < 800 by getting their account_id and sending the message
using Email Message to construct the email body specific to each user.

#Bonus:
for this operation we get the users with flag as pensioner bonus and credit, 10% of their remaining balance as the bonus to the existing balance.Then
we generate the csv file with these details.

#Top users:
this operation is performed by the query where we get all the users and their transcation count which we then partiton by month and rank them according
to the transcation count. From this subquery results we get the top 10 uers for each month and generate the csv file for the same.

#Cash/Digital Ratio:
for this we get the total digital and cash transactions in total for each bank and then we get the top bank with the highest ratio.This was done by 
writing query and also dealing with the null values by assigning the banks to those users who have it as null, by checking their other transcations
with bank name.We have generated a HTML page reporting the ratio details.

#For Setup:
-Have Python, IDE (PyCharm, VS Code, Jupiter etc) installed. 
-Copy the https repo link available from main branch.
-'git repo clone url'  or use get from VCS and use the url.
-Create a branch and work on it.
-install the necessary packages as per the requirements.

#Run the program:
-Run the server.py file first
-Once server is running , copy the server URL and run it from localhost in any suitable browser.
