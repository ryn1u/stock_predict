from twitterscraping import configure_scraper, run_scrape
from tweetspreprocess import preprocess_dataframe
from dateutils import get_workday,get_day
import pandas as pd

import datetime

query = "gme"

start = datetime.datetime.now()

for i in range(-1, 0):

    start = get_workday(i)
    finish = get_day(1, start)

    config, file = configure_scraper(query, 100, start, finish)
    df = run_scrape(config)

    df = preprocess_dataframe(df)
    print(df.head())


finish = datetime.datetime.now()

print(f"START: {start}          FINISH: {finish}")