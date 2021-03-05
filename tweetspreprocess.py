import csv, os
import processtext as ptxt
import pandas as pd
from datetime import datetime

#TO-DO:
#komentarze

def preprocess_dataframe(_dataframe):

    times = dict()
    texts = dict()
    dates = dict()

    counter = 0

    for idx, row in _dataframe.iterrows():

        if not ptxt.isEnglish(row['tweet']):
            _dataframe = _dataframe.drop(idx)
            counter += 1
            continue

        date_and_time_arr = row['date'].split(' ')

        dates[idx] = date_and_time_arr[0]
        times[idx] = date_and_time_arr[1]
        texts[idx] = ptxt.processText(row['tweet'])
        print(f"{dates[idx]} at {times[idx]}: {texts[idx]}")
    
    print(f"\nRemoved {counter} non english entries.\n\n")

    _dataframe = remove_columns(_dataframe)
    _dataframe.insert(0, "date", dates.values(), True)
    _dataframe.insert(1, "time", times.values(), True)
    _dataframe['text'] = texts.values()

    return _dataframe

def save_dataframe(_dataframe, ticker):
    finish = datetime.now()
    time = finish.time().strftime("%H-%M-%S")
    name  = f"data/{ticker}_{finish.date()}_{time}.h5"
    _dataframe.to_hdf(name, key=ticker, mode='w')


def remove_columns(_dataframe):
    keep_columns = ["nlikes", "nreplies", "nretweets"]
    for col in _dataframe.columns:
        if not col in keep_columns:
            _dataframe = _dataframe.drop(columns=col)
    return _dataframe







def preprocess_csv_file(file):
    #removes bad entries from file containg tweets
    new_file = f"processed_scrapes/{file}"
    removed_counter = 0

    with open(file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        fieldnames = ['date', 'time', 'reps', 'rts', 'likes', 'text']
        dialect = 'excel'

        if not os.path.exists(new_file):
            with open(new_file, "w", newline='', encoding="utf-8") as new_csv:
                writer = csv.DictWriter(new_csv, fieldnames=fieldnames, dialect=dialect)
                writer.writeheader()                        #write "fieldnames" at the top of csv file

        with open(new_file, "a", newline='', encoding="utf-8") as new_csv:
            writer = csv.DictWriter(new_csv, fieldnames=fieldnames, dialect=dialect)

            words_counter = 0

            for entry in reader:
                text = ptxt.processText(entry['tweet'])     #removes emojis and redundant whtespace

                if ptxt.isEnglish(text) and len(text) > 0:

                    words_counter += len(text.split())

                    writer.writerow(getEntry(entry, text))
                else:
                    removed_counter += 1
            print(f"Words in file: {words_counter}")
    return new_file, removed_counter

def getEntry(entry, text):
    timestamp = entry['created_at'].split(' ')

    output = {'date': timestamp[0],
            'time': timestamp[1],
            'reps': entry['replies_count'],
            'rts': entry['retweets_count'],
            'likes': entry['likes_count'],
            'text': text}
    
    return output