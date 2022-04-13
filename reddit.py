import praw
import pandas as pd
from praw.models import MoreComments

reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent

# URL of the post
url = "https://www.reddit.com/r/nextfuckinglevel/comments/u1yrwd/play_was_stopped_during_augsburg_vs_mainz_05_so/"

# Creating a submission object
submission = reddit_read_only.submission(url=url)


post_comments = []

for comment in submission.comments:
    if type(comment) == MoreComments:
        continue

    post_comments.append(comment.body)

# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment'])
#comments_df
comments_df.to_json("reddit-comments.json", index=True)
