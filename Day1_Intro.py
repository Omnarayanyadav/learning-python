#sum of two numbers
a= int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
sum =(a+b)
print(sum)


#temperature conversion form deg.celccius to deg.Fahrenheit

C=int(input("Enter the temperature in deg.celcius:"))
Temp= (C*(9/5)+32)
print(Temp)


#Area of rectangle
l= int(input("Enter the length:"))
b= int(input("Enter the breadth:"))
Area=l*b
print(Area)



#printing greeting messages
Name=input("Enter your name:")
Age=int(input("Enter your age:"))
print("Welcome to the world of Programming")



#Even or odd check
num=int(input("Enter the number:"))
check=num%2
if(check==0):
    print("It is even number")
else:
    print("It is odd number")


#find max and min number fom the list of numbers
num = [4, 7, 2, 9, 1, 5, 8, 3, 6]
max = max(num)
min = min(num)

print("Maximum value:", max)
print("Minimum value:", min)

#wap to check palindrome string

# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
    
#compound interest calculation

p=int(input("Enter p:"))
r=float(input("Enter r:"))
t=int(input("Enter t:"))
n=int(input("Enter n:"))

CI=p*(1+r/n)**(n*t)
print("The compound interest is:",CI)

#WAP that converts days into years,weeks,months

day=int(input("Enter the number of days:"))
year=day/365
month=day/30
week=day/7
print("Years:",year)
print("months:",month)
print("Weeks:",week)

#sum of positive integers from the lists of a numbers

num = [1, -2, 3, -4, 5]
sum=0
for n in num:
    if n>0:
      sum+=n
print("Sum of positive integers is:",sum)

#Sentences na count words

sentence=input("Enter the sentence:")
word=len(sentence)
print("Total word in the sentence is:",word)

#swapping

a = input("Enter the value of variable a: ")
b = input("Enter the value of variable b: ")

#values before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

#Swap the values
a, b = b, a

#values after swapping
print("After swapping:")
print("a =", a)
print("b =", b)

