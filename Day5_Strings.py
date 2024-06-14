#program that checks if a given string is palindrome:
def isPalindrome(string): 
    if (string== string[::-1]): 
        return"The string is a palindrome." 
    else: 
        return"The string is not a palindrome." 
 
string=input("Enter string: ") 
print(isPalindrome(string))






#function that counts number of vowels in a string:
def count_vowels(string):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    
    for char in string:
        # If the character is a vowel, increment the count
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

string = input("Enter the string: ")
print("Number of vowels in given string is: ",count_vowels(string))


#cocatenate a list of words into a single sstring:
mylist=['om','narayan','yadav']
str=" ".join(mylist)
print(str)





#function to reverse a string:
def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]
s = input("Enter a string: ")
print("The original string is : ", s)

print("The reversed string is : ",reverse(s))





#program that takes a sentence as input and counts the number of words in it:
def count_words(sentence):
    words=sentence.split(" ")
    return len(words)
sentence=input("Enter a sentence: ")
print("The number of words in the sentence are:",count_words(sentence))






#function that checks if a given string is a pangram (contains all letters of the alphabet)'
import string
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
 
    return True
     
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("True")
else:
    print("False")







#write a function to remove all vowels from string and return the modified string'
def remove_string(string):
    vowels = 'aeiouAEIOU'
    modified_string=''.join([char for char in string if char not in vowels])
    return modified_string
string=input("Enter a string: ")
print("Modified string after removing vowels is: ",remove_string(string))






#Program to find the length of the longest word in a sentence
def length_words(sentence):
    words=sentence.split()
    longest_word=max(words,key=len)
    return longest_word
sentence=input("Enter a sentence: ")
print("The longest words in the sentence are:",length_words(sentence))





#function that takes a sentence as input and returns the sentence in reverse order:
def reverse_sentence(sentence):
    words=sentence.split(" ")
    if len(words)==0:
        return words
    else:
        reversed_words=list(reversed(words))
        return ' '.join(reversed_words)
    
sentence=input("Enter a sentence: ")
reversed_sentence=reverse_sentence(sentence)
print("The reversed sentence is: ",reversed_sentence)        
    
    
    
    
    
#Given a list of names, count the number of names that start with a vowel:
def count_names(names):
    vowel="aeiouAEIOU"
    names_with_vowels=[element for element in names if element[0] in vowel]
    count=len(names_with_vowels)
    return count,names_with_vowels
   
names=["Apple","machine","Learning","pineapple","akash","Natasha","orange","Aryan","Anurag","Analysis","Amarnath","Ganesh"]
count,names_with_wowels=count_names(names)
print("Number of names starting with a vowel are:", count)
print("Names starting with a vowels are:",names_with_wowels)


# Write a function to remove all duplicate characters from a given string:
def duplicate(string):
    return "".join(dict.fromkeys(string))
string=input("Enter a string: ")
no_duplicate=(duplicate(string))
print("String without duplicate charaters is:",(no_duplicate))





# Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence:
def word_checker(sentence,word):
    if word in sentence:
            return True
    else:
            return False
sentence=input("Enter a sentence: ")
word=input("Enter a word to check: ")    
if word_checker(sentence,word):
    print(f"The word {word} is present in sentence.")
    
else:
    print(f"The word {word} is not present in sentence.")