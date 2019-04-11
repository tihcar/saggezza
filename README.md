# saggezza
use cases for saggezza

##### USE CASE 1 #######
##### Read .SQL files from github and run SQL statements in Snowflake through Python

1. download the python script named usecase1.py
2. run " python usecase1.py <github_user> <repo_name> <file_path>
e.g. python usecase1.py tihcar saggezza RRD/usecase1.sql

##### USE CASE 2 #######
##### Send email notification from Python
1. Make sure to download credentials and setup pythone env as mentioned at https://developers.google.com/gmail/api/quickstart/python
2. Run file usecase2.py as " python usecase2.py". It will open a browser window and will ask to login into the email account. Once authenticated the next script can be run. This is a one time process only.
3. Run file usecase2_1.py as "python usecase2_1.py <From> <To> <subject> <Message>
  e.g. python usecase2_1.py rkpabreja@gmail.com rachit.pabreja@saggezza.com test hi
