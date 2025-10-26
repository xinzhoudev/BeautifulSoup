# Print out all the hyperlinks (<a> tags).

import sys, os
# clear the "bs4" mod that has been imported before.
bs4_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(bs4_dir)
for mod in list(sys.modules.keys()):
    if mod.startswith("bs4"):
        del sys.modules[mod]
sys.path.insert(0, bs4_dir)

from bs4 import BeautifulSoup, SoupStrainer, SoupReplacer

filename = "HackerNews.html"
# filename = "psd7003.xml"

# read the <a> tags
only_tags = SoupStrainer("a")
# only parese the specific tags
only_divs = SoupStrainer("div", class_="content")

with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", parse_only=only_tags)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", parse_only=only_tags)

for tag in soup:
    print(tag)