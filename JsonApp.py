#Class library
import json

#Create data dictionary

data1 = {
    'name':'Mileyri Medina',
    'age': 20,
    'city':'Idaho',
    'interests': ['Traveling','Volleyball','Drawing',"Longboarding",'Art','Theology'],
    'is_student': False


}


#Creating a json
with open('data1.json','w') as json_file:
    #Dump data dictonary into data JSON file
    json.dump(data1, json_file, indent=4)


#
print("Data has been written to data1.json")

#Read json file

with open('data1.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Seccessfully able to read data1.json")
print(loaded_data)


#Changing content of json dictionary

loaded_data['age'] = 21
loaded_data['interests'].append('Silly')

#Below is an example of removing an item
#loaded_data['interests'].remove('Silly')

#Resave the altered jason file

with open('data1.json','w') as json_file:
    #Dump data dictonary into data JSON file
    json.dump(loaded_data, json_file, indent=4)


#
print("Data has been re-written to data1.json")