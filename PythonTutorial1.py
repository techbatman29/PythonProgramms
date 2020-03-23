1)#Write a program which will find factors of given number and find whether the factor is even or odd.

num=int(input("Enter the number:"))
f=0
for i in range(2,num):
    if (num%i==0):
        if(i%2==0):
            print("Even Factor",i)
        else:
            print("Odd Factor",i)
        f=1
    if(f==0):
        print("No Factors")
        break

2)#Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically


import numpy as np

a=input("Enter the Sequence:")
a=a.upper()
A=[]
for i in range(0,len(a)):
    A.append(a[i])

print(A)
for i in range(len(A)): 
    for j in range(0, len(A)-i-1): 
        if (A[j]>A[j+1]): 
            A[j]=A[j+1]
	    A[j+1]= A[j] 
  
print(A)   

3)#Write a program that accepts a sentence and calculate the number of letters and digits.

b=input("Enter the Password:")
d=0
w=0
for i in range(0,len(b)):
    temp=b[i]
    if(temp.isdigit()):
        d+=1
    elif(temp.isalpha()):
        w+=1

print(d)
print(w)
    
    
