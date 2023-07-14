import json
jsData = '''{
    "name" : "Mariam",
    "phone" : {
    "type" : "intl",
    "number": "+1 475 233 333"
    },
    "email" : {
    "hide" : "yes"
    }
}'''

jsonInfo  = json.loads(jsData) #load an object of data as a list or dictionary.
print ("Name is", jsonInfo["name"]) #print the name Mariam.
print ("Telfone Number is", jsonInfo["phone"]["number"]) # print the number in phone.

