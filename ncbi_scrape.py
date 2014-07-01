#!/bin/python
from mechanize import Browser
from bs4 import BeautifulSoup

mech = Browser()

#url = "http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=9606708"
#page = mech.open(url)

#html = page.read()
file = open("sample_ncbi.html")
html = file.read()
soup = BeautifulSoup(html)

table = soup.find(id="Allele")
#rows = table.find(lambda tag: tag.name=='td')
rows = table.contents
#print(table)
#print ("printing the rows?")
#print(rows)


#print(soup.prettify())

print "test"
print (table.prettify())

print "testing"
#for row in table:
#    print(row.contents)

print(rows)

#table = soup.find(lambda tag: tag.name=='TABLE' and tag.has_key('id') and tag['id']=="RefSNP") 
#rows = table.find(lambda tag: tag.name=='tr')

#for row in soup.findAll(id='Allele')[0].tbody.findAll('tr'):
#    first_column = row.findAll('th')[0].contents
#    second_column = row.findAll('td')[1].contents
#    print first_column, second_column

