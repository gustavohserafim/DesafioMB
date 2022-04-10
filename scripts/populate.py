import requests
import pandas as pd
from datetime import datetime, timedelta
from time import mktime
from sqlalchemy import create_engine

today = datetime.timestamp(datetime.today())
oldest = mktime((datetime.today() - timedelta(days=365)).timetuple())

pairs = ["BRLBTC", "BRLETH"]

for pair in pairs:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/56.0.2924.76 Safari/537.36 "}

    r = requests.get("https://mobile.mercadobitcoin.com.br/v4/{}/candle?from={}&to={}&precision=1d"
                     .format(pair, int(oldest), int(today)), headers=headers)
    
    if r.status_code == 200:
        candles = r.json()["candles"]

        df = pd.DataFrame(candles)
        df.drop("high", 1, inplace=True)
        df.drop("low", 1, inplace=True)
        df.drop("open", 1, inplace=True)
        df.drop("volume", 1, inplace=True)
        df["pair"] = pair
        df["mms_20"] = round(df["close"].rolling(window=20).mean(), 5)
        df["mms_50"] = round(df["close"].rolling(window=50).mean(), 5)
        df["mms_200"] = round(df["close"].rolling(window=200).mean(), 5)
        df.drop("close", 1, inplace=True)
        df.reset_index(drop=True)
        conn = create_engine("mysql://root:@localhost/desafiomb")
        df.to_sql("pair", con=conn, if_exists="append", index=False)
