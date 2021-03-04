import csv, os
import processtext as ptxt
import pandas as pd

#TO-DO:
#komentarze

def preprocess_dataframe(_dataframe):
    removed_counter = 0

    _dataframe = remove_columns(_dataframe)

    times = []
    for idx, row in _dataframe.iterrows():
        date_and_time_arr = row['date'].split(' ')
        row['date'] = date_and_time_arr[0]
        times.append(date_and_time_arr[1])
    
    _dataframe = _dataframe.insert(1, "time", times, True)
    return _dataframe


def remove_columns(_dataframe):
    keep_columns = ["tweet", "date", "nlikes", "nreplies", "nretweets"]
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