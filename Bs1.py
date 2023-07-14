import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#import ssl

#we can pull out the file we need for it to avoid any error.
#we can ignore the ssl this command
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #input link 
html = urllib.request.urlopen(url).read() #read the information of link as aline
soup =BeautifulSoup(html, 'html.parser') #to check all the page information and parse it, to avoid anything that does not work.

#retrieve all the anchor tags
#The <a> HTML element (or anchor element), with its href attribute, creates a hyperlink to web pages, files, email addresses, locations in the same page, or anything else a URL can address.
tags = soup('a') # to make list of anchor tags
for tag in tags :
    print(tag.get('href', None)) #after href comes the link, this line to get the link or none.