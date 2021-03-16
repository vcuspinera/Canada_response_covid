#!/usr/bin/env python3

##########################################################################
### These tokens are needed for user authentication.                   ###
### Credentials can be generated via Twitter's Application Management: ###
###   https://apps.twitter.com/app/new                                 ###
##########################################################################

# App Name: 
# App ID: 

# Keys and tokens
# Keys, secret keys and access tokens management.
my_keys = {
    'consumer_key' : "xzQYHoHXJcx29TMUjJ4QLnxH9",   # API key
    'consumer_secret' : "Es6gAF423zG6GVqDT4MfqRUzaQACYDCM3HtRImVBJ3elRAdZjz",   # API secret key:
    'access_token_key' : "104295581-MDvqPhWvIFgb8ppUpryJRoODdvHpxBfMhNyeUOnD",   # Access token:
    'access_token_secret' : "XhNgKXPyBgCF0lGNqgkWGOSlYanlx5VYQF8I3bWeYI1t8"   # Access level: Read and write
}

for k in my_keys.values():
    print(k)

# # Access level: Read and write
