import mysql.connector

def parse_to_database(data):
    conn = mysql.connector.connect(user='root', password='wandelBankjePass@123', host='mysql', database='wandelbankje_db')
    print(conn)