from numpy import full
from scrape_comments import *
from process_comments import *
from extract_name_from_url import extract_name_from_url

import pandas as pd
import configparser

secret_config = configparser.ConfigParser()
secret_config.read('secret_config.ini')
REDDIT_KEYS = dict(secret_config['reddit_keys'])


config = configparser.ConfigParser()
config.read('config.ini')
paths = dict(config['paths']) #TODO: DO ALL IN ONE LINE
SAVE_PATH_ROOT = paths['save_comments_path_root']


def scrape_process_and_save_post(post_url:str):
    
    comments = scrape_comments_from_post(
        post_url=post_url,
        reddit_config=REDDIT_KEYS,
    )

    processed_comments = process_comments(comments)

    post_name = extract_name_from_url(post_url)
    print(f'{post_name=}')
    full_save_path = f'{SAVE_PATH_ROOT}{post_name}.csv'
    print(f'{full_save_path=}')
    processed_comments.to_csv(full_save_path)

    # return process_comments(comments)