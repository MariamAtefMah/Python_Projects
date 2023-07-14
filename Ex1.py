str = 'nice day in cairo'
index = str.find('y')
print(index)

sub = str[index+1:]
print(sub)

#value = float(sub)
#print(value) #It will not be able to cahnge it as it is string not a number.

f = open('Test.txt')
di = dict()
for line in f:
    line = line.rstrip() # to remove whitespaces form each line or remove new line from each line \n
    if line =='' : continue
    word = line.split() #to convert the file into list of words
    #if word[0] != 'from' : continue
    print(word[1])
    for i in word :
        di[i]= di.get(i,0) + 1 #to record words into dictionary form
print(di)

maxcount = None 
theword = None
for k,count in di.items() : # count is used to express value in dictionaries, di.items is used to create list of tuples
    if maxcount is None or count > maxcount:
        theword = k
        maxcount = count
print('the maximum word occurences is :', theword, 'with count ', maxcount)

lst = list()
for k,v in di.items() : # to create tuples
    tup = (v,k)
    lst.append(tup)
    # it can be done with this sentence only lst.append((v,k))

lst = sorted(lst, reverse=True)
for v,k in lst[: 10]: #to write most common word from 0 to 9
    print(k,v)