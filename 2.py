#check whether the input character is a vowel,consonant,digit or speccial character
c=input("Enter a character: ")
if c.isalpha():
    if c in "aeiouAEIOU":
        print("It is vowel")
    else:
        print("It is consonant")
elif c.isdigit():
    print("It is a digit")
else:
    print("It is a special character")


#check if the number is odd or even
num = int(input("Enter number: "))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")


#sum of first n numbers
n = int(input("Enter value for n: "))  
s=0 
for i in range(1,n+1):
    s = s+i
print("Sum is ",s)

#Print Odd Numbers from l down to 1 in Reverse
l = int(input("Enter value for l: ")) 
if l%2==0:
    l=l-1
for i in range(l,0,-2):
    print(i,end=" ")


#print all multiples of 5 from 0 to 50
for i in range(0,51,5):
    print(i)
