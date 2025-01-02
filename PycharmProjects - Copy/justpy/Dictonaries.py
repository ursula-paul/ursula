# we use dictionaries when we want to store vales that store value that come as key value pairs
# each key should be unique in a dictionary
# to ways to write a dictionary
# None is an object that defines the absence of a value
from nested_loop import output

client = dict(name="John", email="john@gmail.com", age=33, phone_number=123456, is_verified=True)

customer ={
    "name": "John",
    "email":"john@gmail.com",
    "age":33,
    "phone_number":123456,
    "is_verified": True
}
#customer ["name"] = "Jack Smith"
print(customer ["name"])
customer["birthdate"] = "August 27 2000"
print(customer ["birthdate"])
print(client ["age"])
#print(customer.get("birthdate", "August 27 2000"))
#print(customer ["firstname"])

phone = input("phone:")
digits_mapping ={
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output =  ""
for ch in phone:
    output += digits_mapping.get(ch, "!" ) + " "
print(output)
