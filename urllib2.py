import urllib.request, urllib.parse, urllib.error
fileHandle = urllib.request.urlopen('http://data.pr4e.org/page1.htm') #to open the web like a file to handle it.

for line in fileHandle:
    print(line.decode().strip())

#this code will get the html code form the page1 in this web.