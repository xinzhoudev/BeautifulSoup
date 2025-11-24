# This program is to iterate the BeautifulSoup library.
import os, sys
bs4_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(bs4_dir)
for mod in list(sys.modules.keys()):
    if mod.startswith("bs4"):
        del sys.modules[mod]
sys.path.insert(0, bs4_dir)

from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag

filename = "pretty_sample3.xml"

with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser")
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml")


# print all nodes.
print("*****************************get all of the nodes*****************************")
for node in soup:
    if(isinstance(node, Tag):
        print(node)

print("*****************************get person nodes*****************************")
# simple test node, get html node.
for node in soup:
    if node.name == "person":
        print(node)

print("*****************************get name nodes*****************************")
# test node, get p node.
for node in soup:
    if node.name == "name":
        print(node)

print("*****************************get age nodes*****************************")
# test node, get br node.
for node in soup:
    if node.name == "age":
        print(node)

print("*****************************get email nodes*****************************")
# test node
for node in soup:
    if node.name == "email":
        print(node)


filename = "HackerNews.html"

with open(filename, "r", encoding = "utf-8") as f:
    if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser")
    elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml")


