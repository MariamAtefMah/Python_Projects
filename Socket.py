import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/clown.txt HTTP/1.0\r\n\r\n'.encode() #here we should write an exist file from the web app,
                                                                     #like romeo.txt and clow.txt, data in bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512) #to recieve data up to 512 characters, data in bytes.
    if (len(data)<1):
        break
    print(data.decode()) #to decode recieved data after encoded in sending operation.
    # decode UTF-8 on ASCII code, and this data is unicode
mysock.close()
    

