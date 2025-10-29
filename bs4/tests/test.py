import sys, os
import time
# clear the "bs4" mod that has been imported before.
bs4_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(bs4_dir)
for mod in list(sys.modules.keys()):
    if mod.startswith("bs4"):
        del sys.modules[mod]
sys.path.insert(0, bs4_dir)

from bs4 import BeautifulSoup, SoupStrainer, SoupReplacer

# test case 1: read a html file to test the function.
print("test case 1")
filename = "ArsTechnica.html"
rep = SoupReplacer("a", "a_modified")

with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep)

for tag in soup.find_all("a_modified")[:10]:
    print(tag)

# test case 2: read a xml file to test the function.
print("test case 2")
filename = "pretty_sample3.xml"
rep = SoupReplacer("title", "title_modified")
with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep)
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep)

for tag in soup.find_all("title_modified"):
    print(tag)



