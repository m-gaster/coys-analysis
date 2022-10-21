import pandas as pd
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# DATETIME
def convert_unix_to_datetime(
    comments:pd.DataFrame,
    datetime_col:str='created_utc'
):
    '''
    Alters the dataframe in-place.
    '''
    comments[datetime_col] = pd.to_datetime(comments['created_utc'], unit='s')


# COMMENT SENTIMENT
def analyze_comment_sentiment(comment:str):
    '''
    Analyzes a single comment (using VADER)
    '''
    return SentimentIntensityAnalyzer().polarity_scores(comment)

def analyze_comments_sentiment(comments:pd.Series):
    '''
    Analyzes the sentiment of a series of comments.
    '''
    return comments.apply(analyze_comment_sentiment)

    #TODO: UNPACK DICT TO COLS

def vader_dict_to_cols(comments:pd.DataFrame):

# MAIN
def process_comments(comments:pd.DataFrame):
    '''
    Processes a dataframe of comments.
    '''
    convert_unix_to_datetime(comments)
    comments['sentiment'] = analyze_comments_sentiment(comments['body'])
    return comments