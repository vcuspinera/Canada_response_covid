#!/usr/bin/python

import sys

from twitter import *

config = {}
# execfile("config.py", config)
# execfile("twitter_config.py", config)
execfile("../keys/twitter_config.py", config)

twitter = twitter(auth = OAuth(config["access_token_key"], config["access_token_secret"], config["consumer_key"], config["consumer_secret"]))

# twitter = Twitter(
#     auth = OAuth(config["access_key"], config["access_secret"],
#     config["consumer_key"], config["consumer_secret"]))

query = twitter.search.tweets(q = sys.argv[1])

print ("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))

for result in query["statuses"]:
    print ("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
    # print (result["text"])
