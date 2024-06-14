#function to find factorial of a number:
def factorial(n):
    fact=1
    for i in range(1,(n+1)):
        fact*=i
    print(fact)
factorial(n=int(input("Enter the number:"))) 




#WAF to convert USD to NRP:
def converter(usd_val):
    nrp_val=usd_val*133.57
    print(usd_val,"USD=",nrp_val,"NRP")
converter(100)




#WAF to print length of a list (list is the parameter)
cities=['delhi','dharan','biratnagar','ithari']
def print_len(cities):
    print(len(cities))
print_len(cities)




#WAF to print element of a list in a single line.
cities=['delhi','dharan','biratnagar','ithari','kathmandu',"Inaruwa"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)





#RECURSION
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(7)




#calculation of n!
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
print(fact(6))





#odd even using function
def number(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"
num=int(input("Enter a number: "))
print("The number is: ",number(num))





#sum of first n natural numbers using recursion:
def calc_sum(n):
    if n==0:
        return 0
    return calc_sum(n-1)+n
n=int(input("Enter the value of n: "))
sum=calc_sum(n)
print(sum)




#recursive function which prints all the elements in a list:
def print_list(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","apple","orange","litchi","banana"]
print_list(fruits)





#function to calculate the area of circle:
import math
def calc_area(radius):
    if radius<0:
        raise ValueError("Radius Must be positive")
    return math.pi *radius*radius
radius=float(input("Enter radius: "))
area=calc_area(radius)
print(f"Area of the circle with radius {radius} is {area:2f}")





#function to check if a number is prime or not:
def check_prime(num):
    if num <= 1:
        return (f"{num} is not a prime number")
    if num == 2:
        return (f"{num} is a prime number")
    if num % 2 == 0:
        return (f"{num} is not a prime number")
    
    for i in range(3,int((num)**0.5)+1,2):
        if num % i == 0:
            return (f"{num} is not a prime number")
    
    return (f"{num} is a prime number")

num = int(input("Enter a number: "))
print(check_prime(num))





#Implement a function that reverse a given string:
def reverse_string(str):
    
    return ''.join(reversed(str))
str=input("Enter a string: ")
output=reverse_string(str)
print("The string is reversed and the reversed string is:",output,end=" ")





#function to find the dum of all positive number in a list:
def calc_sum(list):
    positive_numbers=(num for num in list if num>0)
    
    return sum(positive_numbers)
list=[1,2,3,4,5,6,7,-9,-88,-77,-33,-8,-5,4,6,9,11,23,45,-6,77,39,-53]

total_sum=calc_sum(list)
print(total_sum)







#function to check if a given string is a palindrom:
def check_palindrome(string):
    if (string== string[::-1]): 
        return f"{string} is a palindrome." 
    else: 
        return f"{string} is not a palindrome." 
 
#Enter input string 
string=input("Enter string: ") 
 
palindrome=check_palindrome(string)
print(palindrome)






#factorial of a number using recursion:
def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter a number: "))
print(fact(num))






#function to find the square of each element in a list:
def square(list):
    squared_element= (i**2 for i in list)
    return (squared_element)
list1=[1,2,3,4,5,6,7,8,9,10]
squared_list=square(list1)
print(list(squared_list))





#Area of a triangle given its base and height:
def area_triangle(height,base):
    if height and base<=0:
        return "Please enter positive value"
    else:
        return height*base
height=int(input("Enter the height of a Triangle: "))
base=int(input("Enter the base of a Triangle: "))
Area=area_triangle(height,base)
print("Area of Triangle is: ",Area)
    
    
    
    
    
    
#fuction that takes a list of string &
# returs list sorted alphabetically:
def sort_list(list):
    sorted_list=sorted(list)
    return sorted_list

list1=['omega',"omnarayan",'mega',"iphone",'android','snapdragon','blackberry']
sorted_string=sort_list(list1)
print(list(sorted_string))







#function which returns common elements of two lists:
def common(list):
   common_elements=[elements for elements in list1 if elements in list2]
   return common_elements
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2=[2,4,6,8,9,3,5,7,2,11,19,14,17,18,20]
print(common(list))        






#funtion to cheak leap year:
def leap_year(year):
    if year%4==0:
        return True
    elif year%400==0:
        return True
    elif year%100==0:
        return False
    else:
        return False

year=int(input("Enter the year: "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year") 
       
       
       
       

#Function that prints multiplication tables:
def multiplication(num):  
    if num<=0:
        return "Enter positive number"
    table=[]
    for i in range(1,11):
        table.append(f'{num}*{i}={num*i}')
    return table
        
num=int(input("Enter a number: "))
mul_table=multiplication(num)
if isinstance(mul_table,list):
    for line in mul_table:
        print(line)
else:
    print(mul_table)
