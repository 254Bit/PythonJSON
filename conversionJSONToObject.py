# Converting the JSON to a Country Object
# {
#     "name": "Kenya",
#     "currency": "Kshs",
#     "size": 582646,
#     "president": "H.E William Ruto"
# }

# One should be able to access Country Object using the dot operator
import json

class Country:
    def __init__(self, name, currency, size, president):
        self.name = name
        self.currency = currency
        self.size = size
        self.president = president
        
def CountryDecoder(obj):
    return Country(obj['name'], obj['currency'], obj['size'], obj['president'])

countryObj = json.loads('{"name":"Kenya", "currency":"Kshs", "size":582646, "president": "H.E William Ruto"}',
                        object_hook=CountryDecoder)

print('Type of decoded object from JSON Data')
print(type(countryObj))
print('Country Details')
print(countryObj.name, countryObj.currency, countryObj.size, countryObj.president)
print('The country name is',countryObj.name, 'and the currency in',countryObj.currency, 'with a country size of',countryObj.size, 'km.' , 'The president is', countryObj.president)



