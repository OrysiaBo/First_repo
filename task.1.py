print("Hello World")
#list_1 = ["string", 56, 2.4, "Hello", 89, 100]
#print(list_1[0:5:2])
#print(list_1[0], list_1[5])
#print(list_1[::-1])
import datetime  

person: dict = {
    "age": 18,
    "name": "John",
    "birthday": datetime.date(day=26, month=2, year=1995)    
}
#person["age"] = 27
#person["name"] = "Hello"
#print(person["age"])
#print(person["name"])
person.update({"age":27, "name": "Hello"})
print(person["age"])
print(person["name"])