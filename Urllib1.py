import urllib.request, urllib.parse, urllib.error
fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #to open the web like a file to handle it.

for line in fileHandle:
    print(line.decode().strip()) # like in socket, and strip to remove the beginning and end whitespaces.

# this code will retrieve the data inside the romeo file only the second output in socket.