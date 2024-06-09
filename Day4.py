#WAP to ask the user to enter names of 3 favourite fruits and store them in a list:
fruits=[]
fruits.append(input("Enter your 1st favourite fruit: "))
fruits.append(input("Enter your 2nd favourite fruit: "))
fruits.append(input("Enter your 3rd favourite fruit: "))
print(fruits)

#WAP to check if a list contains a palindrome of elements:
list1=[1,2,3,2,5]
list2=["malayalam"]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("Palindrome list:")
else:
    print("NOT Palindrome lis:")


#WAP to count the number of students with grade A in the Tuple:

grade=("C","D","A","A","B","B","A")
print(grade.count("A"))


#store in a list and sort them from A to D:
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)


#Find sum and average using builtin functions form a list of numbers:

list=[2,5,7,9,15,35,98,65,88,75]
total_sum=sum(list)
aveage=total_sum/len(list)
print("Total sum is: ",total_sum)
print("Average is: ",aveage)


#add a new fruits to the list of fruits
fruits=["mango","apple","orange","banana","Grapes"]
fruits.insert(2,"pineapple")
fruits.insert(4,"litchi")
fruits.append("Blue Berry")
print(fruits)

#Accesing elements in tuple using indexing:
tup=(1,5,7,9,11,"orange","banana",5.7)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])

#concatenate two lists of numbers into a single list
list1=[1,3,5,7,9,11,13,15,17,19]
list2=[2,4,6,8,10,12,14,16,18,20]
list=list1+list2
print(list)

#wap to find largest and smallest elements in the list

list1=[1,3,5,7,9,11,13,15,17,19,]
print(max(list1))
print(min(list1))

#function that takes a list of numbers and returns a new list with the squared values:
def list(numbers):
    squared_numbers=[i**2 for i in numbers]
    return squared_numbers
original_list=[1,2,3,4,5]
squared_list=list(original_list)
print("Original list:",original_list)
print("squared list:",squared_list)

#WAP to find common elements between two lists and store them in the new list:
list1=[1,3,5,7,9,11,13,15,17,19,21]
list2=[2,3,5,7,11,13,17,19] 
common_elements=[elements for elements in list1 if elements in list2]
print("Elements in list1:",list1)
print("Elements in list2:",list2)
print("Common elements in list1 and list2 are:",common_elements)


#from a list of words,find the word with maximum length and its length

words=["mouse",'keyboard','mississipi','vocabulary','cryptography','racecar','spelling','incomprehensible','academic']
longest= max(words,key=len)
print("word with maximum length is:",longest)
print("length of word is:",len(longest))


#count the occurrences of each element un the list:
list=[1,3,5,7,3,9,11,7,13,15,5,17,1,19,21,9,4,5,3,1,6,7,4]
occurrence=[]
for element in set(list):
    count=list.count(element)
    occurrence.append((element,count))
print("Occurrences of each element are:")
for element,count in occurrence:
    print(element,"=",count)


#Remove all duplicate names and print the unique names from a lst of names:

names=["om","narayan","Alish","Ankit","Anu","om","sita","Anu","Ram",'Nitu','om','Ankit',"Rahul",'Ram',"Anu",'sita','krishna']
# Convert the list to a set to remove duplicates
unique_names = set(names)

# Convert the set back to a list and sort the names
unique_names_list = sorted(list(unique_names))

# Print the unique names
for name in unique_names_list:
    print(name)

#Create a function that takes a list of strings and returns the list sorted by the length of the strings:

def sort_by_length(strings):
    
    return sorted(strings, key=len)

names=["om","narayan","Alish","Ankit","Anu","sita","Ram",'Nitu',"Rahul",'krishna']
sorted_names = sort_by_length(names)
print("The sorted names are:",sorted_names)


#Write a program that checks if a given list is sorted in ascending order:

def is_sorted_ascending(list):
   
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

list1 = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
print(is_sorted_ascending(list1))  # Output: True

list2 = [1, 13, 2, 4, 5,7,19,44,6,9,77]
print(is_sorted_ascending(list2))  # Output: False


#Implement a function that takes two lists and returns their union (all unique elements from both lists).
def union_lists(list1, list2):
    # Convert lists to sets to remove duplicates
    set1 = set(list1)
    set2 = set(list2)
    
    # Return the union of the two sets
    return list(set1.union(set2))

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2 = [2,4,6,8,10,12,14,16,18,20]
print(union_lists(list1, list2))