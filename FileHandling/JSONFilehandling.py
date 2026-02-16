import json

with open("C:\\Users\\rionb\\PycharmProjects\\Python-seleniun-proj\\Dataformats\\employee.json", 'r') as file:
    data=json.load(file)

print(data)
print(data["name"])

with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\nestedjson.json", 'r') as file:
    data=json.load(file)

email=data["user"]["profile"]["email"]
print(email)

#writing to json file --> dump method()
data={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}


with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\writejson.json", 'w') as file:
    json.dump(data,file)

#update or modify the json file
#read then modify then write back to file
with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\updatejson.json",'r') as file:
    data=json.load(file)
#update the value
data["experience"]=6
#writeback
with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\updatejson.json", 'w') as file:
    json.dump(data,file,indent=4)

