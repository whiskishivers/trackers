#!/usr/bin/python3

import html
import os
import re

# Load all text files in pwd and parse them for torrent tracker-like urls. Output domain list.

tracker_rx = re.compile(r"([A-Za-z]+://)([-\w]+(?:\.\w[-\w]*)+)(:\d+)?/announce")
data = ""
files = [i for i in os.listdir() if i.endswith('.txt')]
urls = set()
domains = set()


# Load data
for i in files:
	with open(i, 'r') as f:
		data += html.unescape(f.read())

# Parse trackers
for i in tracker_rx.finditer(data):
	urls.add(i[0])
	domains.add(i[2])

# Write to full url file
with open('parsed-urls.txt', 'w') as f:
	f.write('\n'.join(sorted(list(urls))))

# Output unique tracker domains
print('\n'.join(sorted(list(domains))))

