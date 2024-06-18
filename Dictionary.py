#creating dictionary:
dict={
    "name":"Omnarayan",
    "percentage": 78,
    "marks":[98,76,66,96,92]
}
print(dict)
print(dict["marks"], dict["percentage"])
print(len(dict))


#dictionary usig dict() constructor:
info= dict(name="Omnarayan",age=22,country="Nepal")
print(info)


#Accesing dictionary:
dict={
    "name":"Omnarayan",
    "percentage": 78,
    "marks":[98,76,66,96,92]
}

x=dict.get("name")
print(x)

#keys()returns list of keys
x=dict.keys()
print(x)

#values() returns list of values:
x=dict.values()
print(x)

#items() returns each item in as tuple in a list:
print(dict.items())

#Change values:
dict["percentage"]=88
print(dict)

#update() updates dictionary:
dict.update({"percentage":91})
print(dict)

#Adding items to dict:
dict={
    "name":"Omnarayan",
    "percentage": 78,
    "marks":[98,76,66,96,92]
}
dict["year"]=2024
print(dict)

#using update()
dict.update({"year1":2025})
print(dict)

#Removing items:
dict={
    "name":"Omnarayan",
    "percentage": 78,
    "marks":[98,76,66,96,92],
    "year":2025
}
print(dict)
dict.pop("year")
print(dict)

dict.popitem()
print(dict)

del dict
print(dict)

dict.clear()
print(dict)


#Looping through dictionary:
dict={
    "name":"Omnarayan",
    "percentage": 78,
    "marks":[98,76,66,96,92]
 }
#prints keys
for x in dict:
    print(x)
#prints values:
for x in dict:
    print(dict[x])
    
#value()method to return values:
for x in dict.values():
    print(x)

#keys()method to return keys;
for x in dict.keys():
    print(x)

#for both keys and values:
for x,y in dict.items():
    print(x,":",y)

#Nested dictionary:
myfamily={
    "child1":{
        "name":"Rambabu",
        "DOB":2004
    },
    "child2":{
        "name":"Shyambabu",
        "DOB":2006
    },
    "child3":{
        "name":"Haribabu",
        "DOB":2009
    }
}

print(myfamily)
print(myfamily["child2"]["name"])

#looping through nested loop:
for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y+ ':',obj[y])

#Three dictionaries inside a dictionary
child1={
        "name":"Rambabu",
        "DOB":2004
    }
child2={
        "name":"Shyambabu",
        "DOB":2006
    }
child3={
        "name":"Haribabu",
        "DOB":2009
    }
myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(myfamily)

#looping through nested loop:
for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y+ ':',obj[y])
