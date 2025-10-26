# Print out all the tags in the document.

import sys, os
# clear the "bs4" mod that has been imported before.
bs4_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(bs4_dir)
for mod in list(sys.modules.keys()):
    if mod.startswith("bs4"):
        del sys.modules[mod]
sys.path.insert(0, bs4_dir)

from bs4 import BeautifulSoup, SoupStrainer, SoupReplacer

# filename = "psd7003.xml"
filename = "HackerNews.html"

# get all the tags. 
all_tags = SoupStrainer()
with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", parse_only=all_tags)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", parse_only=all_tags)

for tag in soup.find_all(True):
    print(tag.name, " ", end="")



