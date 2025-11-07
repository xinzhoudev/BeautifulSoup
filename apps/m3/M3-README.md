Project Title: SoupReplacer

Description: Modify the BeautifulSoup bs4.

1. bs4/\_\_init\_\_.py:

Description: name\_xformer is the transformer of name, attrs\_xformer is the transformer of the attributes, and xformer is arbitrary transformer.

class SoupReplacer:

    def \_\_init\_\_(self, name\_xformer = None, attrs\_xformer = None, xformer = None):

        self.name\_xformer = name\_xformer

        self.attrs\_xformer = attrs\_xformer

        self.xformer = xformer

    def apply(self, tag, attr):

        if isinstance(tag, Tag):

            if self.name\_xformer:

                tag = self.name\_xformer(tag)

                # print("result", tag)

            if self.attrs\_xformer:

                tag = self.attrs\_xformer(tag)

            if self.xformer:

                tag = self.xformer(tag)

            return tag

        if isinstance(tag, str):

            if self.name\_xformer:

                tag = self.name\_xformer(tag)

            if self.attrs\_xformer:

                attr = self.attrs\_xformer(tag, attr)

            if self.xformer:

                tag, attr = self.xformer(tag, attr)

            return tag



2\. bs4/builder/\_htmlparser.py:

    # line 186

    if self.soup.replacer:

        self.soup.replacer.apply(tag, {})



3\. bs4/builder/\_lxml.py:

    # line 393

    if self.soup.replacer:

        tag = self.soup.replacer.apply(tag, final\_attrs)

    # line 427

    if self.soup.replacer:

        name = self.soup.replacer.apply(name, {})

