#!/bin/bash


curl "http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=9606708" 2> /dev/null | 
grep -e '</\?TABLE\|</\?TD\|</\?TR\|</\?TH' |
sed 's/^[\ \t]*//g' | 
tr -d '\n' |
sed 's/<\/TR[^>]*>/\n/g'  |
sed 's/<\/\?\(TABLE\|TR\)[^>]*>//g' |
sed 's/^<T[DH][^>]*>\|<\/\?T[DH][^>]*>$//g' |
sed 's/<\/T[DH][^>]*><T[DH][^>]*>/,/g'

