
print("##Creating Dictionarty")

employ_data = {
 "name": "Jhon",
 "age": 30,
 "department": "Engineering",
 "skills": ["Python", "C+", "Python"]
}



print("##Converting Dictionary to JSON String")


import json

employ_data_json = json.dumps(employ_data, indent=4)
print(employ_data_json)


print("##Writing json to a file")

with open("employ_data.json", "w") as json_file:
 json_file.write(employ_data_json)

print("##Reading form the file")
with open("employ_data.json", "r") as json_file:
 data = json.load(json_file)
 print(data)
