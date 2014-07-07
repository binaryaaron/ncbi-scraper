#!/bin/python
from mechanize import Browser
from bs4 import BeautifulSoup
import sys, getopt 
import csv
import re
import collections



def ncbiUrlBuilder(snp):
""" ncbiUrlBuilder builds the url used by NCBI to query a particular SNP. 
an example url for snp rs96066708 is below:
http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=9606708
and will give the information page for that SNP. It builds the URL based on
the base URL from the ncbi site and concatenates it with some simple string
building tools. 
The URL is passed to mechanize/Browser to open the site, and the opened page
is returned to the program.
Arguments:
snp -- the snp id. 
"""
    #url = "http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=9606708"
    print 'attempting to query', snp
    snpNumber = snp[2:(len(snp))]
    url = "http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?" + "rs=" + snpNumber
    print 'trying url: ' + url 
    mech = Browser()
    page = mech.open(url)
    return page, snp

def tablechopper(pageinfo):
"""tablechopper is the primary workhorse of the program. 
It uses BeautifulSoup to parse the page opened by ncbiUrlBuilder 
and then adds the contents of the Allele table to a list (finalList),
which is returned to the program.
Arguments:
    pageinfo -- list that contains the ncbiUrlBuilder page and the
                snp number.
"""
    soup = BeautifulSoup(pageinfo[0])
    table = soup.find(id="Allele")
    rows = table.contents

    rowlist = []
    for item in rows:
        rowlist.append(item.text)


    #rstrip strips trailing whitespace; these have pesky \n's in them
    rowlist[0] = rowlist[0] + ":" + pageinfo[1].rstrip()

    newlist = []
    for item in rowlist:
        newlist.append(item.split(':'))
#    headerList = []
    finalList = []
    for item in newlist:
        #        headerList.append(item[0])
        finalList.append(item[1])
    return(finalList)


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"thi:o:",["ifile=","oufile="])
    except getopt.GetoptError:
        print 'usage: ncbi_scrape.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: ncbi_scrape.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt == '-t':
            print 'entering test mode, using sample_ncbi.html'
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print 'inputfile is', inputfile
    print 'outputfile is', outputfile


    with open(inputfile) as f:
        for line in f:
            html = ncbiUrlBuilder(line)
            writeAllele = tablechopper(html)
            print ",".join(writeAllele)
            length = len(writeAllele)
            with open(outputfile, "a") as writefile:
                writer = csv.writer(writefile, delimiter=',')
                writer.writerow(writeAllele)

    print 'done'

if __name__ == "__main__":
    main(sys.argv[1:])
