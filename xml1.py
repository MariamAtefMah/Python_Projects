import xml.etree.ElementTree as ET #to use this by writting only ET

#''' to write the xml code this is like { }.
data = '''<person> 
    <name>Mariam</name>
    <phone type="intl"> +1 734 303 4456</phone>
    <email hide ="yes"/>
</person>'''
tree = ET.fromstring(data) #this line send the tree form of the xml code to parse it later.
print('Name:', tree.find('name').text) #thise will print Mariam only
print('Attribute:', tree.find('email').get('hide'))
print('Phone', tree.find('phone').get('intl')) 