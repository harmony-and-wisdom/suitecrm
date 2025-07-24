import json
import  mysql.connector
from datetime import datetime

with open(r'..\data\view_accounts_data.json', 'r') as f:
    data = json.load(f)


conn = mysql.connector.connect(
    host = "127.0.0.1",
    port = "3306",
    user = "root",
    password = "Password@97",
    db = "MysuiteCRM"
)
print(conn.is_connected())
#
cursor = conn.cursor()

#create table

create_table_query = '''
CREATE TABLE IF NOT EXISTS account_data (
    Name VARCHAR(100),
    City VARCHAR(100),
    Billing_Country VARCHAR(100),
    Phone VARCHAR(20),
    User_Name VARCHAR(100),
    Email_Address VARCHAR(100),
    Date_Created DATETIME
)
'''
cursor.execute(create_table_query)
conn.commit()

# insert query
insert_query = '''
INSERT INTO account_data 
(Name, City, Billing_Country, Phone, User_Name, Email_Address, Date_Created)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''

for item in data:

    date_obj = datetime.strptime(item["Date Created"], "%m/%d/%Y %I:%M%p")

    values = (
        item["Name"],
        item["City"],
        item["Billing Country"],
        item["Phone"],
        item["User"],
        item["Email Address"],
        date_obj
    )
    cursor.execute(insert_query, values)

conn.commit()
print("Data inserted successfully.")
