import yfinance as yfin
import sqllite_operation as sql
import requests
import pandas as pd
import io
import os


def get_all_taiwan_stocks():
    url = 'https://mops.twse.com.tw/server-java/t105sb02'
    payload = {
        'firstin': 'true',
        'step': 10,
        'filename': 't51sb01_20241013_192008233.csv'
    }
    response = requests.post(url, data=payload)
    response.encoding = 'big5'
    df = pd.read_csv(io.StringIO(response.text), encoding='utf-8')
    return df


def get_stock(stock_id):
    return yfin.download(stock_id, '2000-01-01')


def insert_sqlite():
    sql.create_table()
    stocks = get_all_taiwan_stocks()
    for index, stock_row in stocks.iterrows():
        stock_id = str(stock_row['公司代號']) + '.tw'
        df = get_stock(stock_id)
        df = df.reset_index(drop=False)
        for index, row in df.iterrows():
            sql.add_record(stock_row['公司代號'], stock_row['公司簡稱'], stock_row['產業類別'],
                           row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'],
                           row['Volume'])


if __name__ == '__main__':
    stocks = get_all_taiwan_stocks()
    for index, stock_row in stocks.iterrows():
        stock_id = str(stock_row['公司代號']) + '.tw'
        df = get_stock(stock_id)
        df = df.reset_index(drop=False)
        df['公司代號'] = stock_row['公司代號']
        df['公司簡稱'] = stock_row['公司簡稱']
        df['產業類別'] = stock_row['產業類別']
        output_path = './stock/' + str(stock_row['公司代號']) + '.csv'
        df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
