import xml.etree.ElementTree as ET #to use this by writting only ET

#''' to write the xml code this is like { }.
input = '''<person>
    <users> 
        <user x="2">
            <id>01</id>
            <name>Mary</name>
        </user>  
        <user x="3">
            <id>02</id>
            <name>Hoppa</name>
        </user>
    </users>
</person>'''

treeOfXml = ET.fromstring(input)
lst = treeOfXml.findall('users/user') #save a list of all users.
print("User count", len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute', item.get("x"))
    print('----------------')



    