import twint
from datetime import datetime
import pandas as pd

#TO-DO:
#uzupełnianie o brakujące wpisy???
#export to pandas(conditional with option to save in csv)

def configure_scraper(query, limit, since, until, save_to_pandas=True):
    #used for configuring twitter search and saving results to a CSV file
    c = twint.Config()

    c.Search = query
    c.Lang = "en"
    c.Limit = limit
    c.Hide_output = True

    c.Since = since.isoformat()
    c.Until = until.isoformat()

    #output configuration
    file_format = "" if save_to_pandas else ".csv"
    timenow = datetime.now().strftime("%H%M%S")             #timestamp for unique output file naming
    output_string = f"{query}_{since}_{timenow}{file_format}"#output file name
    c.Custom["tweet"] = ["created_at", "replies_count", "retweets_count", 
    "likes_count", "tweet"]   

    if save_to_pandas:
        c.Store_csv = False
        c.Pandas = True
    else:
        c.Store_csv = True
        c.Pandas = False
        c.Output = output_string

    c.Count = True

    return c, output_string

def run_scrape(config):
    twint.run.Search(config)

    if config.Pandas:
        return twint.storage.panda.Tweets_df