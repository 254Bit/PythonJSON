# <-------- Converting this Country object into JSON ----------->

# import json
# class Country:
#     def __init__(self, name, currency, size, president):
#         self.name = name
#         self.currency = currency
#         self.size = size
#         self.president = president
        
# Country = Country('Kenya', 'Kshs', 582646)

from json import JSONEncoder
import json

class Country:
    def __init__(self, name, currency, size, president):
        self.name = name
        self.currency = currency
        self.size = size
        self.president = president

class CountryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

Country = Country('Kenya', 'Kshs', 582646, 'H.E William Ruto') 

print('Encoding Country Object into a JSON')
CountryJson = json.dumps(Country, indent =4, cls=CountryEncoder)
print(CountryJson)
