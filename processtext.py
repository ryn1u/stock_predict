# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

#TO-DO:
#komentarze

def isEnglish(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def removeURLs(text):
    return re.sub(r"http\S+", "", text)

def removeAts(text):
    return re.sub(r"@\S+", "", text)

def removeWhitespace(text):
    return re.sub(' +', ' ', text)

def leaveLettersAndNumbers(text):
    return re.sub('[\W_]+', ' ', text)

def processText(text):
    return leaveLettersAndNumbers(removeWhitespace(removeAts(removeURLs(deEmojify(text)))))