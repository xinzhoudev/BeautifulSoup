Project Title:



Part-2: Find the location.

Description: Find the location of the functions used in milestone1 and part-1 of milestone2.

1\. find\_all(): line 2715, col 217 in element.py file.

2\. get(): line 2160, col 12 in element.py file.

3\. get\_text(): line 524, col 17 in element.py file.

3\. prettify(): line 2601, col 17 in element.py file.

3\. find\_parent(): line 992 col 20 in element.py file.

4\. select\_one(): line 2782 col 19 in element.py file.

4\. select(): line 2799 col 16 in element.py file.

5\. class SoupStrainer(): line 313 col 19 in filter.py file.



Part-3: Modify in BS4:

1. \_\_init\_\_: add the SoupReplacer() class(It contains \_\_init\_\_ and replace() methods), and the new parameter replacer.

    1.1. class SoupReplacer(): line 132 in bs4/\_\_init\_\_.py

    1.2. SoupReplacer.\_\_init\_\_(): line 133 in bs4/\_\_init\_\_.py

    1.3. SoupReplacer.replace(): line 136 in bs4/\_\_init\_\_.py

    The full code is: 

&nbsp;   class SoupReplacer:

&nbsp;       def \_\_init\_\_(self, og\_tag, alt\_tag):

&nbsp;           self.og\_tag = og\_tag

&nbsp;           self.alt\_tag = alt\_tag

&nbsp;       def replace(self, name):

&nbsp;           if name == self.og\_tag:

&nbsp;               return self.alt\_tag

&nbsp;           else:

&nbsp;               return name



2\. Builder/\_lxml.py: modify the start() and end() method.

    2.1. start(): tag = self.soup.replacer.replace(tag): line 394 in bs4/builder/\_lxml.py

    2.2. end(): name = self.soup.replacer.replace(name): line 429 in bs4/builder/\_lxml.py

&nbsp;   The full code is:

&nbsp;   if getattr(self.soup, "replacer", None):

&nbsp;       tag = self.soup.replacer.replace(tag)

&nbsp;   if getattr(self.soup, "replacer", None):

&nbsp;       name = self.soup.replacer.replace(name)





3\. Builder/\_htmlparser.py: handle\_starttag() and handle\_endtag().

    3.1. handle\_starttag(): name = self.soup.replacer.replace(name): line 183 in bs4/builder/\_htmlparser.py

    3.2. handle\_endtag(): name = self.soup.replacer.replace(name): line 217 in bs4/builder/\_htmlparser.py

&nbsp;   The full code is:

&nbsp;   if self.soup.replacer:

&nbsp;       name = self.soup.replacer.replace(name)

&nbsp;   if self.soup.replacer:

&nbsp;       name = self.soup.replacer.replace(name)

