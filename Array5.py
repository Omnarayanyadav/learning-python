#Accessing array using for loop with index
from array import *
stu_roll = array('i',[101,102,103,104,105])

n = len(stu_roll)
for i in range(n): 
    print("index",i, stu_roll[i])