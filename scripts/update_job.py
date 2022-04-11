import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from time import mktime


def get_db_con():
    return create_engine("mysql://desafiomb:desafiomb@mysql/desafiomb")


def update():
    pairs = ["BRLBTC", "BRLETH"]

    for pair in pairs:
        today = datetime.timestamp(datetime.today())
        oldest = mktime((datetime.today() - timedelta(days=365)).timetuple())

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/56.0.2924.76 Safari/537.36 "}

        r = requests.get(
            f"https://mobile.mercadobitcoin.com.br/v4/{pair}/candle?from={int(oldest)}&to={int(today)}&precision=1d",
            headers=headers
        )

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

            today_data = df.iloc[-1]

            engine = get_db_con()
            with engine.connect() as con:
                today_data.to_sql("pair", con=con, if_exists="append", index=False)


if __name__ == '__main__':
    update()
