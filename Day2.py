#variable for storing a persons name,age and average test scores.
name=input("Enter your name:")
Age=int(input("Enter your age:"))
Average_test_score=float(input("Enter your average test score:"))
print("Name:",name)
print("Age:",Age)
print("Average_test_score:",Average_test_score )

#concatenate two strings
string1="Om"
string2="narayan"
concatenate=string1+string2
print(concatenate)

#list of fruits and access using indexing

fruits=["apple","orange","pineapple","grapes","mango","banana"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[5])

#given list of number find sum and average
mylist=[1,4,5,6,9,8,3,6,7,8,4,2]
total_sum=sum(mylist)
count=len(mylist)
average=total_sum/count
print("sum:",total_sum)
print("Average:",average)
#celcius into kelvin

temp=float(input("Enter the temperature in celcius:"))
kelvin=temp+273.15
print("Temperature in Kelvin is:",kelvin)

#wap to check palindrome string

#Define a function 
def isPalindrome(string): 
    if (string== string[::-1]): 
        return"The string is a palindrome." 
    else: 
        return"The string is not a palindrome." 
 
#Enter input string 
string=input("Enter string: ") 
 
print(isPalindrome(string))


#reverse string

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]


s = "panama"

print("The original string is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

#concatenate list into a string

mylist=['om','narayan','yadav']
mystring=' '
for a in mylist:
    mystring=mystring+' '+a
print(mystring)

#concatenate list into a string join method
mylist=['om','narayan','yadav']
str=" ".join(mylist)
print(str)


#Check if the string is pangram
import string
 
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
 
    return True
     
    # Driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("True")
else:
    print("False")

#area and circumference of a circle when radius is given:
import math
r=float(input("Enter the radius of circle: "))
area=math.pi*r*r
circumference=2*math.pi*r
print("Area of a cicle is: ",area)
print("Circumference of a circle is: ",circumference)

#minutes into minutes and hours
minute=int(input("Enter the minutes: "))
hours=minute//60
minutes=minute%60
print("Total Hours is:",hours)
print("Total minutes is: ",minutes)

#function to count number of vowels in a string
def count_vowels(string):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    
    for char in string:
        # If the character is a vowel, increment the count
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

string = input("Enter the string: ")
print("Number of vowels in given string is: ",count_vowels(string))  # Output should be 3


#check prime number
number = int(input("Enter a number: "))
is_prime = True
# Check if the number is less than 2 (not prime)
if number < 2:
    is_prime = False
else:
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(number, "is a prime number.")
else:
    print(number ,"is not a prime number.")
