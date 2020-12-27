import csv
import re


# creates our sentiment library
def make_sentiment_dict():
    sentiment = {}
    with open("sentiment/afinn.csv") as csvfile:
        egg = csv.reader(csvfile)
        for i, row in enumerate(egg):
            if i != 0:
                sentiment[row[0]] = int(row[1])

    return sentiment


# sanitize and tokenize a given string
def prep_text(text):
    text = text.lower()
    result = re.findall(r"\w+[\-\_\*\']*\w*", text)
    return result


# fix the word not
def gauge_sentiment(tokens, sentiment_data):
    tally = 0
    for token in tokens:
        if token in sentiment_data:
            tally += sentiment_data[token]

    return tally


def sentiment_analyze(text, sentiment_dict):
    tokens = prep_text(text)
    tally = gauge_sentiment(tokens, sentiment_dict)
    return tally


if __name__ == "__main__":
    print("hello!")
    sentiment = make_sentiment_dict()
    prepped = sentiment_analyze("i fucking HATE sheldon bot", sentiment)
    print(prepped)