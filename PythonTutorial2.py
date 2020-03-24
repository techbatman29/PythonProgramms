""" You will find some basic problems using Sequences Concepts(Strings and Dictionary) and Pattern """


1)#Checking the Password Strength Check 

Password=input('Enter the password:')

a=0
A=0
d=0
c=0
m=0
M=0

for i in range(0,len(Password)):
    temp=Password[i]
    if(temp.isdigit()):
        d+=1
    elif(temp.islower()):
        a+=1
    elif(temp.isupper()):
        A+=1
    if(temp == '$'):
       c+=1
    elif(temp == '/'):
       c+=1
    elif(temp == '@'):
       c+=1

if(d>=1 & a>=1 & A>=1 & c>=1 & (len(Password)>=6 & len(Password)<=12)):
    print("Password Strong")
else:
    print("Password Weak")

2)#Write a program which count and print the numbers of each character in a string input by console.Example: If the following string is given as input to the program:abcdefgabc

Word = "abcdeabcefgi"
Freq = {} 
  
for i in Word: 
    if i in Freq: 
        Freq[i] += 1
    else: 
        Freq[i] = 1

print(Freq)

3)#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=(i)/(i+1)
