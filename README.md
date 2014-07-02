# NCBI Scraper
Python script to aggregate data from NCBI. I will add comments to the program soon, Sara, but i'd just let it run overnight for now. 
Basic usage is as such:

	python ncbi_scrape.py -i rsnumbers.csv -o ncbi_rs_list.csv

and will require the following python pacakges:
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
* [Mechanize](http://wwwsearch.sourceforge.net/mechanize/)

and I reccomend you install them using [Pip](https://pypi.python.org/pypi/pip) using the following commands:
	pip install bs4
	pip install mechanize

and it should run just fine from there. 
