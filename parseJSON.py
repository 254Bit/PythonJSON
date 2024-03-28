#Parsing a JSON to get all the values of a key 'name' within an array

import json

sampleJson = """[
    {
    "id": 1,
    "name": "Kenya",
    "color": [
    "Red",
    "Green",
    "Black"
    ]
    },
    {
    "id": 2,
    "name": "Uganda",
    "color": [
    "Yellow",
    "Black",
    "Red"
    ] 
    }
]"""
data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)