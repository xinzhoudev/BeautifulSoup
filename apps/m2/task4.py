# Task-4: Print out all the tags that have an id attribute. (this should be done with a single API call)
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
# only preserve the contents with id
id_strainer = SoupStrainer(attrs={"id": True})

with open(filename, "r", encoding="utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", parse_only=id_strainer)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", parse_only=id_strainer)

for tag in soup.find_all(True):  
    tag_id = tag.get("id")
    if tag_id:
        print(f"Tag: {tag.name}, id: {tag_id}")