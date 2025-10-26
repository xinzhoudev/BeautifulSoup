import sys, os
# clear the "bs4" mod that has been imported before.
bs4_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(bs4_dir)
for mod in list(sys.modules.keys()):
    if mod.startswith("bs4"):
        del sys.modules[mod]
sys.path.insert(0, bs4_dir)

from bs4 import BeautifulSoup, SoupStrainer, SoupReplacer

rep = SoupReplacer("b", "blockquote")
filename = "HackerNews.html"
# filename = "pretty_sample3.xml"

with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep)

for tag in soup.find_all("blockquote"):
    print(tag)

# test case 1:
print("test case 1")
filename = "pretty_sample3.xml"
rep = SoupReplacer("name", "NameTag")
with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep)

for tag in soup.find_all("NameTag"):
    print(tag)

# test case 2:
print("test case 2")
filename = "test.html"
rep = SoupReplacer("b", "blockquote")
with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep)

for tag in soup.find_all("blockquote"):
    print(tag)
