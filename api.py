import praw
import json
import re

with open("users.json") as file:
    userDetails = json.load(file)

CLIENT_ID = userDetails["CLIENT_ID"]
CLIENT_SECRET = userDetails["CLIENT_SECRET"]
USERNAME = userDetails["USERNAME"]
PASSWORD = userDetails["PASSWORD"]
USER_AGENT = userDetails["USER_AGENT"]

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USER_AGENT,
                     username=USERNAME)

#print(reddit.user.me())
outputFile = open("redditOutputs.txt","a+")
subreddit = reddit.subreddit('FloridaMan')
subredditList = subreddit.top('all')
list_iterator = iter(subredditList)
next(list_iterator)

for submission in list_iterator:
    #print(submission.title)
    if bool(re.match("Florida Man", submission.title, re.I)) == True or bool(re.match("Florida Woman", submission.title, re.I)) == True:
        outputFile.write(submission.title + "\n")
    else:
        next(list_iterator)

outputFile.close()
