Title: Learn Installation and Repository setup.



First, build a repository in GitHub: BeautifulSoup, and copy its path https://github.com/xinzhoudev/BeautifulSoup.git.



Second, push files to the repository:

1. Find out the correct directory in my computer;(It depends on the specific file path of the computer)
2. git init : initiate the directory.
3. git remote add origin https://github.com/xinzhoudev/BeautifulSoup.git
4. git status: To check the current status of the directory: it should be "branch master", which means it is the master branch.
5. git add . : Stage all the changes.
6. git commit -m "Initial Commit": To commit changes.
7. git push origin master



Third, release the repository.

1. Open the url of the repository. https://github.com/xinzhoudev/BeautifulSoup
2. Click the "Code" tag in the top of the menu, and click "Release" button.
3. Click "Draft a new release" button. 
4. Select Tag "milestone-2", and input the Release Title = "milestone-2".
5. Click "Publish Release" button.





\# BeautifulSoup

Beautiful Soup is a library that makes it easy to scrape information

from web pages. It sits atop an HTML or XML parser, providing Pythonic

idioms for iterating, searching, and modifying the parse tree.



\## Environment Setup and Installation



\#### Download the repository from Canvas course page



```bash

~/> cd beautifulsoup

```

\#### Create ```Conda``` environment and activate it inside ```~/beautifulsoup``` directory

```bash

\# python=3.10 is required

:~/ cd beautifulsoup

beautifulsoup:~/ conda create -n bs4 python=3.10

beautifulsoup:~/ conda activate bs4

```



\## OR



\#### Create ```Venv``` environment and activate it inside ```~/beautifulsoup``` directory

```bash

\# python=3.10 is required

:~/ cd beautifulsoup

beautifulsoup:~/ python3 -m venv venv

beautifulsoup:~/ source venv/bin/activate  # On macOS/Linux

```



\#### Install all dependencies with pytest

```bash

beautifulsoup:~/ pip install -e .

beautifulsoup:~/ pip install pytest

```





\#### Run Test

```bash

\#  If you are using conda env

cd beautifulsoup

beautifulsoup:~/ pytest

```

```bash

\# if you are using venv env

cd beautifulsoup/bs4/tests

beautifulsoup/bs4/tests:~/ pytest

```



\## Github Repository Setup (GitHub CLI)

\- Install \[GitHub CLI](https://cli.github.com/) and configure it with your GitHub Account 

\- Checkout this to learn \[Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

\- The following approach is with \[GitHub CLI](https://cli.github.com/)

```bash

:~/ cd beautifulsoup

beautifulsoup:~/ git init

beautifulsoup:~/ git add .

beautifulsoup:~/ git commit -m "Initialize Repository" 

beautifulsoup:~/ gh repo create beautifulsoup --source=. --public --push

```



\## Github Repository Setup (GitHub Web)

\- In your GitHub web account, create a repository named beautifulsoup. 

\- It will generate a repository link: https://github.com/YOUR-USERNAME/beautiful.git

\- Now open a terminal inside the downloaded ```beautifulsoup``` folder and steup the repository

\- \*\*\* Replace ```YOUR-USERNAME``` with your GitHub username.



```bash

:~/ cd beautifulsoup

beautifulsoup:~/ git init

beautifulsoup:~/ git commit -m "repository initialization"

beautifulsoup:~/ git branch -M main

beautifulsoup:~/ git remote add origin https://github.com/YOUR-USERNAME/beautiful.git

beautifulsoup:~/ git push -u origin main

```







\# Quick start



```

>>> from bs4 import BeautifulSoup

>>> soup = BeautifulSoup("<p>Some<b>bad<i>HTML")

>>> print(soup.prettify())

<html>

&nbsp;<body>

&nbsp; <p>

&nbsp;  Some

&nbsp;  <b>

&nbsp;   bad

&nbsp;   <i>

&nbsp;    HTML

&nbsp;   </i>

&nbsp;  </b>

&nbsp; </p>

&nbsp;</body>

</html>

>>> soup.find(string="bad")

'bad'

>>> soup.i

<i>HTML</i>

\#

>>> soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")

\#

>>> print(soup.prettify())

<?xml version="1.0" encoding="utf-8"?>

<tag1>

&nbsp;Some

&nbsp;<tag2/>

&nbsp;bad

&nbsp;<tag3>

&nbsp; XML

&nbsp;</tag3>

</tag1>

```



To go beyond the basics, \[comprehensive documentation is available](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).



\# Links



\* \[Homepage](https://www.crummy.com/software/BeautifulSoup/bs4/)

\* \[Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

\* \[Discussion group](https://groups.google.com/group/beautifulsoup/)

\* \[Development](https://code.launchpad.net/beautifulsoup/)

\* \[Bug tracker](https://bugs.launchpad.net/beautifulsoup/)

\* \[Complete changelog](https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/CHANGELOG)

















