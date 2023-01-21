#!/usr/bin/python3

import html
import os
import re
from urllib.parse import unquote

# Read .txt files in cwd, get tracker-like urls and output domains.

tracker_rx = re.compile(r"([A-Za-z]+://)([-\w]+(?:\.\w[-\w]*)+)(:\d+)?/announce")
data = ""
files = [i for i in os.listdir() if i.endswith('.txt')]
urls = set()
domains = set()

for i in files:
	with open(i, 'r') as f:
		data = unquote(html.unescape(f.read()))

	for i in tracker_rx.finditer(data):
		urls.add(i[0])
		domains.add(i[2])

print('\n'.join(sorted(list(domains))))

# Save full urls
with open('parsed-urls.txt', 'w') as f:
	f.write('\n'.join(sorted(list(urls))))

