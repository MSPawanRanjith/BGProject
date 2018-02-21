import json

#print ("hello pawan ")
#x=input("Enter the Name : ")
#print(x)
#x=eval(input("Enter list with comma sepereated "))
#print(x)
#name=input("Name :")
#print (name)

with open('data.txt') as json_file:  
    data = json.load(json_file)
    #for p in data:
        #print('Name: ' + p['patient_no'])
        #print('Website: ' + p['patient_name'])
        #print('From: ' + p['patient_BG_values'])
        #print('')
    print(data)
