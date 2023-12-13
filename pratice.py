##Reversing a String using an Extended Slicing Technique
##string="python programme"
##print(string[7:])
##Counting Vowels in a Given Word
##vowle=("a,e,i,o,u")
##word="programme"
##count=0
##for i in word:
##    if i in vowle:
##        count+=1
##print(count)
##Counting Consonants in a Given Word
##vowle=("a,e,i,o,u")
##word="programme"
##count=0
##for i in word:
##    if i not in vowle:
##        count+=1
##print(count)
##Counting the Number of Occurances of a Character in a String
##word="python"
##charcter="P"
##count=1
##for i in word:
##    if charcter==word:
##        count+=1
##print(count)
##Writing Fibonacci Series
##a=0
##b=1
##num=int(input("enter the value of number"))
##for i in range(num):
##    result=a+b
##    a=b
##    b=result
##    print(a)
## Finding the Maximum Number in a List
##list1=[80,650,89,12,45]
##a=list1[0]
##for i in list1:
##    if a < i:
##        a = i
##print(a)
####Finding the Minimum Number in a List    
##list1=[80,650,89,12,45]
##b=list1[0]
##for i in list1:
##    if b > i:
##        b = i
##print(b)
## Finding the Middle Element in a List
##list1=[1,2,3,4,5,6,2,3,8,5,4]
##length=len(list1)
##value=int(length/2)
##print(list1[value])
##11. Converting a List into a String
##list1=["p","y","t","h","o","n"] 
##b="".join(list1)
##print(b)
##print(type(b))
## Adding Two List Elements Together
##list1=[1,2,3]
##list2=[4,5,6]
##list3=[]
##for i in range(0,len(list1)):
##    list3.append(list1[i]+list2[i])
##print(list3)
##13. Comparing Two Strings for Anagrams
##str1 = "Listen"
##str2 = "Silent"
##
##str1 = list(str1.upper())
##str2 = list(str2.upper())
##str1.sort()
##print(str1)
##str2.sort()
##print(str2)
##if(str1 == str2):
##    print("True")
##else:
##    print("False")
##14. Checking for Palindrome Using Extended Slicing Technique
##
##str1 = "Kayak".lower()
##str2 = "kayak".lower()
##if(str1 == str2):
##    print("True")
##else:
##    print("False")
##  15. Counting the White Spaces in a String
##string="p rogra mm e"
##print(string.count(' '))
###Counting Digits, Letters, and Spaces in a String
##import re
##name = "Python is 1 s"
##digitcount=re.sub("[^0-9]","",name)
##lettercount=re.sub("[^A-Z]","[^a-z]","",name)
##print(name.count(' '))
##print(len(digitcount))
##print(len(lettercount))
##Counting Special Characters in a String
##import re
##spChar = "!@#$%^&*()"
##count=re.sub("[\w]","",spChar)
##print(len(count))
##Building a Pyramid in Python
##num=int(input("enter the value of number"))
##for i in range(num):
##    for j in range(num-i):
##        print(" ",end="")
##    for k in range(i+1):
##        print("*",end=" ")
##    print("")

##Randomizing the Items of a List in Python
from random import shuffle
lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)


















