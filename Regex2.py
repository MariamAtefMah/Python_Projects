import re
#ex1
s = 'Data Structure 2 is hard to learn 45 but fun to use 6'
y = re.findall(' [0-9]+', s)
print(y)

#ex2
x = 'Data Structure: is hard to learn:  but fun to use'
d= re.findall('^D.+:', x)
print(d)

#ex3
e = 'Data Structure: is hard to learn:  but fun to use'
f = re.findall('^D.+?:', e) #it will stop at the first whitespace appear in the line, as it means does not end with :
print(f)

#ex4
a = 'Data Structure:is hard to learn:  but fun to use'
b = re.findall('Data (\S+:\S+)', a) #it will write the line till learn: and stop and wont write Data.
print(b)

#ex5
aa = 'The price of skin care is $2000.00 and $503.00 for Hair care'
bb = re.findall('\$[0-9.]+', aa) #it will write the line till learn: and stop and wont write Data.
print(bb)