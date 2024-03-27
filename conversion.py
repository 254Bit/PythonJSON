# Convert a dictionary into JSON Format

import json
dictionary_list = [{'ID1': 'Olivia', 'Profession': 'Data Analyst', 'Age': 37}, 
                 {'ID2': 'Terry', 'Profession': 'Nurse', 'Age': 40}, 
                 {'ID3': 'Dora', 'Profession': 'Vetinary', 'Age': 34},
                 {'ID4': 'Alicia', 'Profession': 'Software Developer', 'Age': 29}]
jsondata = json.dumps(dictionary_list)
print(jsondata)

# sampleJson = {'ID1': 'Olivia', 'Code2': 'Data Analyst'}
# data =json.loads(sampleJson) # converted to dictionary
# data['ID1']