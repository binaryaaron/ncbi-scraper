#!/bin/python
from mechanize import Browser
from bs4 import BeautifulSoup
import sys, getopt 
import argparse
import csv
import re
import collections



def ncbiUrlBuilder(snp):
    """ncbiUrlBuilder builds the url used by NCBI to query a particular SNP. 
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
    #checks to see if the type None was applied to the beautifulsoup object
    #if so, it returns nothing
    if table == None:
        print 'allele id not found or merged; adding NA to csv'
        errorlist = [pageinfo[1].rstrip(), 'NA','NA','NA','NA','NA','NA','NA']
        return errorlist
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

def searchfile(fname):
    txtFile = open(fname, "r")
    searchList = []
    for line in txtFile:
        line_split = line.rstrip("\n").split(',')
        searchList.append(line_split[0])
    return searchList

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "NCBI Scraper")
    parser.add_argument('-i', "--inputfile", metavar='inputfile',
                        nargs='+', help='the input file')
    parser.add_argument('-o', "--outputfile", metavar='outputfile', 
                        nargs='+', help = 'the file to which output will be written')
    args = parser.parse_args()
    inputfile = args.inputfile[0]
    outputfile = args.outputfile[0]
    print 'the inputfile is', inputfile
    print 'the outputfile is', outputfile

    searchlist = searchfile(outputfile)
#    print searchlist
    with open(inputfile) as f:
        for line in f:
            if line.rstrip("\n") not in searchlist:
                html = ncbiUrlBuilder(line)
                writeAllele = tablechopper(html)
                print ",".join(writeAllele)
                length = len(writeAllele)

                with open(outputfile, "a") as writefile:
                    writer = csv.writer(writefile, delimiter=',')
                    writer.writerow(writeAllele)
            else:
                print 'found the number already in outputfile, skipping', line

    print 'done'

