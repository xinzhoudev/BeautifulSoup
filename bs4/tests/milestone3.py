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


# 1. rename the tag
def test_tag_rename(filename):
    # input the name_xformer function.
    # rename the "b" tag as "mm" tag.
    def rename_html(tag):
        if tag.name == "a":
            tag.name = "mm"
        return tag
    rep_html = SoupReplacer(name_xformer=rename_html)
    def rename_xml(tag):
        if tag == "name":
            return "mm"
        return tag
    rep_xml = SoupReplacer(name_xformer=rename_xml)

    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep_html)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep_xml)
    for tag in soup.find_all("mm"):
        print("test1", tag)

# test_tag_rename("pretty_sample3.xml")
test_tag_rename("HackerNews.html")	

# 2. remove an existing attribute.
def test_attr_remove(filename):
    # remove the tag attribute.
    def xf_html(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    rep_html = SoupReplacer(xformer=xf_html)
    def xf_xml(tag, attrs):
        if "class" in attrs:
            print("Find the class")
            del attrs["class"]
        return tag, attrs
    rep_xml = SoupReplacer(xformer=xf_xml)
    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep_html)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep_xml)
    for tag in soup.find_all(attrs={"class": True}):
        print(tag)
    print("test2 result is listed above, and it should be none.")

# test_attr_remove("HackerNews.html")
test_attr_remove("pretty_sample3.xml")


# 3. return new attributes
# if tag.name == "p" then return {"id":"replaced"} else tag.attrs
def test_attrs_xformer_returns_new_attrs(filename):
    def xf_html(tag):
        if tag.name == "tr":
            return {"id":"replaced"}
        else:
            return tag.attrs
    rep_html = SoupReplacer(attrs_xformer=xf_html)
    def xf_xml(tag, attrs):
        if tag == "person":
            attrs["class"] = "replaced"
        return tag, attrs
    rep_xml = SoupReplacer(attrs_xformer=xf_xml)
    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep_html)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep_xml)

    if(filename.lower().endswith(".html")):
        for tag in soup.find_all(attrs={"id":True}):
            print("test3", tag)

    if(filename.lower().endswith(".xml")):
        for tag in soup.find_all(attrs={"class":True}):
            print("test3", tag)


test_attrs_xformer_returns_new_attrs("HackerNews.html")
test_attrs_xformer_returns_new_attrs("pretty_sample3.xml")

# 4. combine the name_xformer and attrs_xformer together.
def test_combined_name_and_attrs(filename):
    """
        name_xformer + attrs_xformer at the same time
    """
    def rename_html(tag):
        if tag.name == "span":
            tag.name = "div"
        return tag
    def attrs_xf_html(tag):
        if tag.name == "div":
            tag["class"] = "new"
        return tag
    rep_html = SoupReplacer(name_xformer=rename_html, attrs_xformer=attrs_xf_html)
    
    def rename_xml(tag):
        if tag == "name":
            return "lala"
        else:
            return tag
    def attrs_xf_xml(tag, attrs):
        if tag == "person":
            attrs["class"] = "test4"
        return tag, attrs
    rep_xml = SoupReplacer(name_xformer=rename_xml, attrs_xformer=attrs_xf_xml)

    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep_html)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep_xml)
    for tag in soup.find_all("div"):
        print("test4", tag)
    for tag in soup.find_all("lala"):
        print("test4", tag)

# test_combined_name_and_attrs("HackerNews.html")
test_combined_name_and_attrs("pretty_sample3.xml")


# 5. rename the tag by xformer rather than name_xformer.
def test_xformer_modify_on_name(filename):
    # replace the tag.name "p" with "section".
    def xform_html(tag):
        if tag.name == "a":
            tag.name = "section"
    rep_html = SoupReplacer(xformer=xform_html)
    def xform_xml(tag, attrs):
        if tag == "name":
            tag = "section"
        return tag, attrs
    rep_xml = SoupReplacer(xformer=xform_xml)
    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep_html)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep_xml)
    for tag in soup.find_all("section"):
        print("test5", tag)

test_xformer_modify_on_name("HackerNews.html")
test_xformer_modify_on_name("pretty_sample3.xml")

# 6. no replacer means no real function in the fields. Test the robustness of the SoupReplacer.
def test_noop_replacer(filename):
    """If no transformer provided, soup unchanged."""
    rep = SoupReplacer()
    with open(filename, "r", encoding = "utf-8") as f:
        if(filename.lower().endswith(".html")): soup = BeautifulSoup(f, "html.parser", replacer=rep)
        elif(filename.lower().endswith(".xml")): soup = BeautifulSoup(f, "lxml-xml", replacer=rep)
    for tag in soup.find_all(True):
        print("test6", tag)

test_noop_replacer("HackerNews.html")
test_noop_replacer("pretty_sample3.xml")
