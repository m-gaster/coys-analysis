import pandas as pd
import yaml
from datetime import datetime
import praw

def load_config(config_path, return_=False):
    global config
    with open(config_path, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            for k, v in config.items():
                globals()[k] = v
            # print(config)
        except yaml.YAMLError as exc:
            print(exc)
    if return_:
        return config

secret_config_path = '../../secret_config.yaml'
config_path = 'config.yaml'
load_config(config_path)
secret_config = load_config(
    secret_config_path,
    return_=True
    )


def scrape_comments_from_post(post_url:str, config=secret_config) -> pd.DataFrame:
    reddit = praw.Reddit(**config)
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)
    comments = submission.comments.list()
    return pd.DataFrame([ vars(post) for post in comments ])


### DATA PROCESSING ###
def extract_time_from_comments(comments:pd.DataFrame):
    # comments['created_utc'] = comments['created_utc'].apply(unix_to_timestamp)
    comments['created_utc'] = pd.to_datetime(comments['created_utc'], unit='s')


def analyze_comment_sentiment(comment:str) -> float:
    # https://huggingface.co/blog/sentiment-analysis-python
    # https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis?text=what+is+sonny%27s+problem
    # https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
    pass

def create_sentiment_col()