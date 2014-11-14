# NCBI Scraper
Python script to aggregate data from NCBI made for a friend in Anthropology. 

Basic usage is as such:

	python ncbi_scrape.py -i rsnumbers.csv -o ncbi_rs_list.csv

and will require the following python pacakges:
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
* [Mechanize](http://wwwsearch.sourceforge.net/mechanize/)

and I reccomend you install them using [Pip](https://pypi.python.org/pypi/pip) using the following commands:

	pip install beautifulsoup4
	pip install mechanize

and it should run just fine from there. Note that it will check the csv file
specified for output to make sure it's not inserting a duplicate record and
will notify you that it found a duplicate.

I'd let this run overnight or as long as it takes to collect your data. 
If you get any errors, NCBI could have banned your IP address or something -
let me know.  
