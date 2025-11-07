#!/usr/bin/env python
# coding: utf-8
# name_xformer = name_transformer

import sys, os

# clear the "bs4" mod that has been imported before.
bs4_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print(bs4_dir)
for mod in list(sys.modules.keys()):
    if mod.startswith("bs4"):
        del sys.modules[mod]
sys.path.insert(0, bs4_dir)

from bs4 import BeautifulSoup, SoupStrainer, SoupReplacer
from bs4.element import Tag
import bs4
print(bs4.__file__)


# task-7: Find all the <p> tags and add (or replace) a class attribute class="test" then write the tree onto a file.

# 1. rename the tag
def find_p_and_replace_class(filename):
    # input the name_xformer function.
    # rename the "b" tag as "mm" tag.
    def html(tag):
        if tag.name == "p":
            # print(tag)
            tag["class"] = "test"
        return tag
    rep_html = SoupReplacer(xformer=html)
    def xml(tag, attrs):
        if tag == "name":
            attr["class"] = "test"
        return tag
    rep_xml = SoupReplacer(name_xformer=xml)

    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep_html)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep_xml)
    for tag in soup.find_all("p"):
        print("test7", tag)

# find_p_and_replace_class("pretty_sample3.xml")
find_p_and_replace_class("ArsTechnica.html")	


