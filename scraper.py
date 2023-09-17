import praw
from praw.models import MoreComments
import pandas as pd

reddit = praw.Reddit(client_id="",		 
							client_secret=""	 ,
			user_agent="Web Scraper project")	

subreddit = reddit.subreddit("Programming")


#by posts in subreddit
posts = []
for submission in reddit.subreddit("india").hot(limit=20):
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        posts.append(top_level_comment.body)
posts = pd.DataFrame(posts,columns=["body"])
posts.to_csv("rising.csv",index=True)



# by month
posts_ = subreddit.top("month")

posts_dict = {"Title": [], "Post Text": [],"Total Comments": [], "Post URL": []}

for post in posts_:
	posts_dict["Title"].append(post.title)
	posts_dict["Post Text"].append(post.selftext)
	posts_dict["Total Comments"].append(post.num_comments)
	posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)
 
top_posts.to_csv("TopPosts.csv", index=True)

#url
url = "https://www.reddit.com/r/learnprogramming/comments/16kqe3b/im_addicted_to_programming/"
submission = reddit.submission(url=url)
posts__ = []
for top_level_comment in submission.comments[1:]:
    if isinstance(top_level_comment, MoreComments):
        continue
    posts__.append(top_level_comment.body)
posts__ = pd.DataFrame(posts__,columns=["body"])
indexNames = posts__[(posts__.body == '[removed]') | (posts__.body == '[deleted]')].index
posts__.drop(indexNames, inplace=True)
print(posts__)
