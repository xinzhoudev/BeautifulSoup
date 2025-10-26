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

\_\_init\_\_: add the SoupReplacer() class(It contains \_\_init\_\_ and replace() methods), and the new parameter replacer.

&nbsp;   1. class SoupReplacer(): line 132 in bs4/\_\_init\_\_.py

&nbsp;   2. SoupReplacer.\_\_init\_\_(): line 133 in bs4/\_\_init\_\_.py

&nbsp;   3. SoupReplacer.replace(): line 136 in bs4/\_\_init\_\_.py

Builder/\_lxml.py: modify the start() and end() method.

&nbsp;   1. start(): tag = self.soup.replacer.replace(tag): line 394 in bs4/builder/\_lxml.py

&nbsp;   2. end(): name = self.soup.replacer.replace(name): line 429 in bs4/builder/\_lxml.py

Builder/\_htmlparser.py: handle\_starttag() and handle\_endtag().

&nbsp;   1. handle\_starttag(): name = self.soup.replacer.replace(name): line 183 in bs4/builder/\_htmlparser.py

&nbsp;   2. handle\_endtag(): name = self.soup.replacer.replace(name): line 217 in bs4/builder/\_htmlparser.py

