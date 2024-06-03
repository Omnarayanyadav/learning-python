#check positive negative or zero
num=int(input("Enter the number: "))
if num>0:
    print(num,"Is positive number")
elif num<0:
    print(num, "Is negative number:")
else:
    print("It is Zero")

#loop that prints first 10 even numbers
n=10
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1

#using for loop
n=10
i=1
for i in range(1,n+1):
    if i%2==0:
        print(i)

#program to find the largest number in a list
num_list = [3, 5,9,11,7,14,106.277,588,76,233]
if not num_list:  # Check if the list is empty
    largest = None
else:
    largest = num_list[0]  # Assume the first number is the largest initially
    for number in num_list:
        if number > largest:
            largest = number  
print("The largest number in the list is: ",largest)

#leap year program

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year," is a leap year.")
        else:
            print(year,"is not a leap year.")
    else:
        print(year,"is a leap year.")
else:
    print(year," is not a leap year.")

#even numbers from list
mylist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even_number=(num for num in mylist if num%2==0)
even_numbers=list(even_number)
print("Even numbers in the list are: ",even_numbers)

#prime number check:
num=int(input("Enter the number:"))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

#fibonacci sequence
term=int(input("Enter the number of terms: "))
n1,n2=0,1
count=0
if term<=0:
    print("Please enter positive term!!")
elif term==1:
    print("Fibonnaci sequence upto",term,":")
    print(n1)
else:
    print("Fobonnaci sequence: ")
    while count<term:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


#printing names from a list which are starting from A:

names=["Apple","Aman","om","akash","Natasha","Nisha","Aryan","Anurag","Anuradha","Amarnath","Ganesh"]
a_names=[elements for elements in names if elements.startswith("A")]
print("Names stsrting with A are: ",a_names)


#multiplication table of n numbers using while loops
n=int(input("Enter the number you want the table of: "))
i=1
while i<=10:
    print(n*i)
    i+=1


#multiplication table of n numbers using for loops
n=int(input("Enter the number you want the table of: "))
for i in range(1,11):
    print(n*i)


#factorial using while loop
n=int(input("Enter the number: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    
print("Factorial is: ",fact)

#using for loop

n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial is:",fact)
    

#prime number check:
for num in range(1,51):
    is_prime=True
    if num<2:
        is_prime=False 
    else:
        for i in range(2,num):
            if num%i==0:
              is_prime=False
              break
    if is_prime:
           print(num)
         

#count number of words more than five characters in the list:

names=["Apple","machine","Learning","pineapple","akash","Natasha","orange","Aryan","Anurag","Analysis","Amarnath","Ganesh"]
count=0
for char in names:
    if len(char)>5:
        print(char)
        count+=1
print("Number of words with more than five characters are:",count)


#sum of digits of a given numbers:
num=int(input("Enter the number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print("Total sum is:",sum)

#using while loop
num=int(input("Enter the number:"))
sum=0
i=0
while i<=num:
    sum+=i
    i+=1
print("Total sum is:",sum)
