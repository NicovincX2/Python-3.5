# -*- coding: utf-8 -*-

import os

from bs4 import BeautifulSoup  # For HTML parsing
import urllib2  # Website connections
import re  # Regular expressions
# Filter out stopwords, such as 'the', 'or', 'and'
from nltk.corpus import stopwords


def text_cleaner(website):
    '''
    This function just cleans up the raw html so that I can look at it.
    Inputs: a URL to investigate
    Outputs: Cleaned text only
    '''
    try:
        site = urllib2.urlopen(website).read()  # Connect to the job posting
    except:
        return   # Need this in case the website isn't there anymore or some other weird connection problem

    soup_obj = BeautifulSoup(site)  # Get the html from the site

    if len(soup_obj) == 0:  # In case the default parser lxml doesn't work, try another one
        soup_obj = BeautifulSoup(site, 'html5lib')

    for script in soup_obj(["script", "style"]):
        script.extract()  # Remove these two elements from the BS4 object

    text = soup_obj.get_text()  # Get the text from this

    lines = (line.strip() for line in text.splitlines())  # break into lines

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    text = ''.join(chunk for chunk in chunks if chunk).encode(
        'utf-8')  # Get rid of all blank lines and ends of line

    # Now clean out all of the unicode junk (this line works great!!!)

    try:
        # Need this as some websites aren't formatted
        text = text.decode('unicode_escape').encode('ascii', 'ignore')
    # in a way that this works, can occasionally throw
    except:
        return                                                         # an exception

    # Now get rid of any terms that aren't words (include 3 for d3.js)
    text = re.sub("[^a-zA-Z+3]", " ", text)
    # Also include + for C++
    # Fix spacing issue from merged words
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

    text = text.lower().split()  # Go to lower case and split them apart

    stop_words = set(stopwords.words("english"))  # Filter out any stop words
    text = [w for w in text if not w in stop_words]

    # Last, just get the set of these. Ignore counts (we are just looking at
    # whether a term existed
    text = list(set(text))
    # or not on the website)

    return text

os.system("pause")
