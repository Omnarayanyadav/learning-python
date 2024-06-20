#creating a set:
myset={"apple","banana","orange"}
print(myset)
print(len(myset))
print(type(myset))



#data types in sets:
set1={"apple","banana",20,66.5,True}
print(set1)



#duplicate values are not accepted:#True and 1 are considered as same and so as false and 0:
set1={True,False,1,0,"om"}
print(set1)  #output is {True,False,"om"}



#using set() constructor to create a set:
myset=set(("apple",'banana','mango'))
print(myset)



#Accessing items in set: directly cannot be accessed so using for loop:
set1={"apple","banana","orange",'mango'}
for x in set1:
    print(x)
    
#check if mango is present:
print("mango" in set1)

#check if banana is not present in set:
print("banana" not in set1)


#Add items to set:
set1={"apple","banana","orange",'mango'}
set1.add("papaya")
print(set1)

#Add items from another set to current set use update() method:
set1={"apple","banana","orange",'mango'}
set2={"pineapple",'papaya','litchi'}
set1.update(set2)
print(set1)

#Add elements of a list to a set:
set1={"apple","banana","orange",'mango'}
list1=["pineapple",'papaya','litchi']
set1.update(list1)
print(set1)


#Remove items:to remove use remove() or discard() method
set1={"apple","banana","orange",'mango'}
set1.remove("banana")  #if item to remove doesn't exists than it will rise an error.
print(set1)
set1.discard("banana")  #if item to remove doesn't exists than it will not rise an error.
print(set1)
#using pop() method but it will remove a random item.
set1.pop()
print(set1)

#clear() method empities the set and del keyword deletes the set:
set1={"apple","banana","orange",'mango'}
set1.clear()
print(set1)
del set1   #output will show name_error as set has been deleted
print(set1)

#loop tems:
myset={"apple","banana","orange"}
for i in myset:
    print(i)


#Join sets:
#union() method
set1={1,2,3,4}
set2={'a','b','c','d'}
set3=set1.union(set2)
print(set3)
#using | operator as union()
set3=set1|set2
print(set3)

#join multiple sets:
set1={1,2,3,4}
set2={'a','b','c','d'}
set3={"apple","banana","orange"}
set4={True,False}
myset=set1.union(set2,set3,set4)
print(myset)
#using | operator
myset1=set1|set2|set3|set4
print(myset1)

#join a set and a tuple:
x={'a','b','c','d'}
y=(1,2,3,4)   #union() method allows to join set with other data types like list or tuple
z=x.union(y)
print(z)

#update() method:inserts all items from one set into another:
set1={1,2,3,4}
set2={'a','b','c','d'}
set1.update(set2)
print(set1)

#intersection() method:returns set that contains common elements of both sets:
set1={1,3,5,7,9,11,13,15,17,19}
set2={2,3,5,7,11,13,17,19}
set3=set1.intersection(set2)
print(set3)
#if we use & operstor instead of intersection() it will give same output:
set4=set1&set2
print(set4)

#intersection_update():change origial set insteda of retuning new set:
set1={1,3,5,7,9,11,13,15,17,19}
set2={2,3,5,7,11,13,17,19}
set1.intersection_update(set2)
# set1 &= set2 this will also give the same result
print(set1)

#difference():returns new set that will contains only items from first set and discard common items:
set1={"apple","banana","orange"}
set2={"micrsoft","google","apple"}
set3=set1.difference(set2)
#set3=set1 - set2 will also give same result:
print(set3)
set1.difference_update(set2)
print(set1)

#symmetric_difference():returns set of items that are not peresent in both sets:
set1={"apple","banana","orange"}
set2={"micrsoft","google","apple"}
set3=set1.symmetric_difference(set2)
#set3=set1^set2 will also give same result
print(set3)
set1.symmetric_difference_update(set2)
print(set1)

