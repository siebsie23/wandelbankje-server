import pymysql

def parse_to_database(data):
    conn = pymysql.connect(host='mysql', port=3306, user='root', passwd='wandelBankjePass@123', db='wandelbankje_db')
    print(conn)