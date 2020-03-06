import pandas as pd 
import re
#read_html module in pandas can be used to read html pages
#and to run that we need html5lib
import html5lib
url="https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_A"
url_read=pd.read_html(url,header=0)[0]
#re module =whitespace character remove in a file(regular expression)
space=re.compile(r"\s+") #expression for regular expression for finding space r = raw string 

#function
def fix_string_spaces(column_to_fix):
    temp_column_name=[]
    for item in column_to_fix:
        if space.search(item):
            temp_column_name.append('_'.join(space.split(item))) #will join _ in place of the space
        else:
            temp_column_name.append(item)
    return temp_column_name

url_read.columns=fix_string_spaces(url_read.columns)

print(url_read.head(10)[['IATA','Airport_name']])
