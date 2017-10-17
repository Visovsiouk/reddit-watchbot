import praw

reddit = praw.Reddit(client_id='your_id',
                     client_secret='your_client_secret_key',
                     password='your_user_password',
                     username='your_user_name',
                     user_agent = "Reddit Bot for watching titles")

hintcache = []

def hint_bot():
    while True:
        subreddit = reddit.subreddit("soccer")
        for submission in subreddit.stream.submissions():
            title = submission.title.lower()
            if submission not in hintcache:
                if 'match' in title and 'thread' in title:
                    for friend in reddit.user.friends():
                        reddit.redditor(friend.name).message('Brand new /r/soccer Match Thread', 'Game: ' + submission.selftext + '\n\n' + 'Url: ' + submission.url)