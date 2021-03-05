from twitterscraping import configure_scraper, run_scrape
from tweetspreprocess import preprocess_dataframe, save_dataframe
from dateutils import get_workday,get_day
import pandas as pd

import datetime

query = "gme"

begin = datetime.datetime.now()

for i in range(-7, 0):

    start = get_workday(i)
    finish = get_day(1, start)

    config, file = configure_scraper(query, 10000, start, finish)
    df = run_scrape(config)

    df = preprocess_dataframe(df)

    save_dataframe(df, query)

finish = datetime.datetime.now()
print(f"START: {begin}          FINISH: {finish}")