import pymysql

def connectdb():
    print("连接到mysql服务器...")
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        passwd="eop1005.",
        port=3306,
        db="eop_mysql",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("连接成功！")
    return db

connectdb()



