import pandas as pd
import yaml
import praw


# def load_config(config_path:str, return_=False):
#     with open(config_path, "r") as stream:
#         try:
#             config = yaml.safe_load(stream)
#             for k, v in config.items():
#                 globals()[k] = v
#             # print(config)
#         except yaml.YAMLError as exc:
#             print(exc)
#         if return_:
#             return config
        

# secret_config_path = '../../secret_config.yaml'
# secret_config = load_config(
#     secret_config_path,
#     return_=True
# )

def scrape_comments_from_post(post_url:str, reddit_config) -> pd.DataFrame:
    reddit = praw.Reddit(**reddit_config)
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)
    comments = submission.comments.list()
    return pd.DataFrame(
        [vars(post) for post in comments]
    )