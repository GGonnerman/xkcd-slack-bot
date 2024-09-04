from sender import send_updated_xkcd
import feedparser 
from os.path import exists
import time

XKCD_URL = "https://xkcd.com/rss.xml"
feed = feedparser.parse(XKCD_URL)

most_recent_entry = feed.entries[0]

# Grab the ID and see if that was the most recently processed comic
# If so, exit right away
id = most_recent_entry['id']

filename="sequence_file.txt"
if exists(filename):
    with open(filename, "r") as f:
        file_contents = f.read()
        if file_contents == id: exit()

# Grab key fields and send them in a message
title = most_recent_entry['title']
summary = most_recent_entry['summary']
image_url = summary.split('src="')[1].split('"')[0]
alt_text = summary.split('alt="')[1].split('"')[0]
published_parsed = most_recent_entry['published_parsed']
published = time.strftime("%a, %B %d", published_parsed)
#print(title, image_url, published)

send_updated_xkcd(title, image_url, alt_text, published)

# Update the most recently processed comic
with open(filename, "w") as f:
    f.write(id)
