#Storing word and its meanings in a dictionary:
dictionary={
    "cat": "a small animal",
    "table": ["a piece of furniture","list of facts and figures"]
}
print(dictionary)


#Enter marks of 3 subjects from user and store them in a dictionary
marks={}
x=int(input("Enter marks of physics: "))
marks.update({"Phy":x})

x=int(input("Enter marks of Chemistry: "))
marks.update({"Chem":x})

x=int(input("Enter marks of Maths:  "))
marks.update({"Maths":x})

print(marks)


#way to store 9 & 9.0 as seperate values in a set.
values={9,"9.0"}
print(values)
values1={
    ("float",9.0),
    ("int",9)
}
print(values1)

#Create a dictionary to store information about a person (name, age, address).
info={
    "name":"Omnarayan Yadav",
    "Age":22,
    "Address":"Sunsari"
}
print(info)

#Adding new key-value pair 
info["Education"]="Engineering"
print(info)


#create a set of unique numbers from a list of numbers
numbers=[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
unique_numbers=set(numbers)
print(unique_numbers)


#Given two dictionaries, merge them into a single dictionary 
dict1={"name":"ram","age":25}

dict2={"address":"Sunsari","Programme":"BEI"}

dict1.update(dict2)
print(dict1)


#Implement a function that removes a key-value pair from a dictionary
def remove_key_value_pair(d,key):
    if key in d:
        del d[key]
    return d
fruits={"1":"Mango","2":"Banana","3":"Orange","4":"Litchi"}
key_to_remove="3"
updated_dict=remove_key_value_pair(fruits,key_to_remove)
print(updated_dict)


#Create a program that checks if two sets have any elements in common 
def check_common(set1,set2):
        common_elements=set1.intersection(set2)
        if common_elements:
            return common_elements
        else:
            return "NO common elements found"
set1={1,2,3,4,5,6,7,8,9}
set2={1,3,5,7,9,11}
result=check_common(set1,set2)
print(result)


#Given a list of dictionaries, find the dictionary with the highest value for a specific key 
def highest_value_dict(dicts,key):
    return max(dicts,key=lambda x:x.get(key,float("infinity")))

dictionaries= [
    {'name': 'Ram', 'age': 22},
    {'name': 'Hari', 'age': 25},
    {'name': 'krishna', 'age': 29},
    {'name': 'Balmukund', 'age': 28}
]
key="age"
result=highest_value_dict(dictionaries,key)
print(result)



#Write a Python program that counts the number of occurrences of each character 
# in a given string using a dictionary 
def count_character(string):
    
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
            
    return char_count
string=input("Enter a string: ")
frequency=count_character(string)
print(frequency)



#Given two sets, find the union, intersection, and difference between them 
set1={"apple","banana","orange"}
set2={"micrsoft","google","apple"}

set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)

set5=set.difference(set2)
print(set5)


#Create a function that takes a list of dictionaries and sorts them based on a specified key 
def sort_dictionary(dicts,key):
    return sorted(dicts,key=lambda x: x[key])

dictionaries= [
    {'name': 'Ram', 'age': 22},
    {'name': 'Hari', 'age': 25},
    {'name': 'krishna', 'age': 29},
    {'name': 'Balmukund', 'age': 28}
]
key="name"
result=sort_dictionary(dictionaries,key)
print(result)



# Write a program that finds the average value of all the elements in a list of dictionaries
def calc_average(dicts,key):
    values=[d[key] for d in dicts if key in d]
    total=sum(values)
    average=total/len(values) if values else 0
    return average

dictionaries= [
    {'name': 'Ram', 'age': 22},
    {'name': 'Hari', 'age': 25},
    {'name': 'krishna', 'age': 29},
    {'name': 'Balmukund', 'age': 28}
]

key='age'
average_age=calc_average(dictionaries,key)
print(f"The average age is {average_age}")



# Implement a function that takes a list of strings and
#returns a set of unique characters present in all strings
def unique_char(strings):
    if not strings:
        return set()
    common_characters=set(strings[0])
    for string in strings[1:]:
        common_characters.intersection_update(string)
    return common_characters

strings=["apple","banana","orange","papaya"]
result=unique_char(strings)
print(result)