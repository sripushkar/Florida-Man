import requests
import json

#Name of the subreddit
subreddit = "r/floridaman"
#Enter either new or top here
sort_type = "top"
#How many posts you want to retrieve
post_limit = "5"

url = "https://www.reddit.com/"+subreddit+"/search.json?q=florida_man&limit="+sort_type+"&sort="+post_limit+"&restrict_sr=1"

results = requests.get(url)
print(results.text)
