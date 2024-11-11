import sqlite3 as lite


def operate_db(sql):
    con = lite.connect('stock.db')
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS STOCK (
        ID INTEGER PRIMARY KEY autoincrement,
        STOCK_ID TEXT,
        STOCK_NAME TEXT,
        STOCK_TYPE TEXT,
        DATE  TEXT,
        OPEN  TEXT,
        HIGH  TEXT,
        LOW   TEXT,
        CLOSE TEXT,
        ADJ_CLOSE TEXT,
        VOLUME INTEGER
    );
    '''
    operate_db(sql)


def add_record(STOCK_ID, STOCK_NAME, STOCK_TYPE, DATE, OPEN, HIGH, LOW, CLOSE, ADJ_CLOSE, VOLUME):
    sql = '''
    INSERT INTO STOCK (STOCK_ID, STOCK_NAME, STOCK_TYPE, DATE, OPEN, HIGH, LOW, CLOSE, ADJ_CLOSE, VOLUME)
    VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {});
    '''
    operate_db(sql.format(STOCK_ID, STOCK_NAME, STOCK_TYPE, DATE, OPEN, HIGH, LOW, CLOSE, ADJ_CLOSE, VOLUME))


def query_record(userid):
    sql = '''
    SELECT * FROM STOCK WHERE STOCK_ID = '{}';
    '''
    con = lite.connect("stock.db")
    cur = con.cursor()
    cur.execute(sql.format(userid))
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows
