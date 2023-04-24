"""
1. Write a program that asks the user for an http/s address, and later, extracts all existing http addresses 
from that website and saves them in a file called urls.txt (one line for each address).
"""

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

email_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
fresult = open(path + "/urls.txt", 'w')

with urllib.request.urlopen('http://python.org/') as response:
    charset = response.info().get_content_charset()
    html = response.read().decode(charset)
    emails = re.findall(email_pattern, html)

for email in emails:
    fresult.write(email + "\n")


"""
2. Write a program that prompts the user for an http/s address, and then extracts all 
existing http addresses in links on that website and stores them in a file called href.txt (one line for each address).
"""

url = input('Enter url: ')      #http://python.org/
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
fresult = open(path + "/href.txt", 'w')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   fresult.write(tag.get('href', None) + "\n")


"""
3. Modify the above program to act recursively up to a level depth of 5 levels
"""