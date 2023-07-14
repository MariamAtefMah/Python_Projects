import json
jsData = '''[
    {
    "id" : "22",
    "number" : "3",
    "name" : "Mariam"
    },
    {
    "id" : "44",
    "number" : "1",
    "name" : "Abdo"
    }
]'''

info = json.loads(jsData)
print('Number of customers is', len(info))
for item in info:
    print('Name', item['name'])
    print('Number', item['number'])
    print('Id', item['id'])
    print('-------------------')


