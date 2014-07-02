# NCBI Scraper
Python script to aggregate data from NCBI. I will add comments to the program soon, Sara, but i'd just let it run overnight for now. 
Basic usage is as such:

	python ncbi_scrape.py -i rsnumbers.csv -o ncbi_rs_list.csv

and will require the following python pacakges:
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
* [Mechanize](http://wwwsearch.sourceforge.net/mechanize/)

and I reccomend you install them using [Pip](https://pypi.python.org/pypi/pip) using the following commands:

	pip install beautifulsoup4
	pip install mechanize

and it should run just fine from there. 


## TODO
Right now, the program will only read the list of rsnumbers (rsnumbers.csv) and will not check to see if it has already
done a number. I could add this support if you want it, but you could easily use a tool like 'uniq' or something
to delete multiples if you need to. sorry about that. 

I'd let this run overnight. If you get any errors, NCBI could have banned your IP address or something. who knows.
