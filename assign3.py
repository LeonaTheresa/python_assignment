#Write a python program to find the sum of the cosine series 1- x^2/2! + x^4/4!-...
import math
x=int(input("Enter value of x:"))
n=int(input("enter no of terms:"))
sum=0.0
for i in range(0,n,2):
    fac=math.factorial(i)
    sum+=((x**2)/fac)
print(sum)


#Write a python program to generate the following type of pattern for the given N rows where N <= 26.
''' A
    A B
    A B C D 
    A B C D E
'''
n=int(input("enter no of rows:"))
for i in range(n+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()


#Write a python program to generate prime numbers within a certain range
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
for num in range(lower_limit, upper_limit + 1):
    if num<=1:
        continue
    prime=True
    for i in range(2,int(num**0.5)+1):       
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,end=" ")


#Write a Python program to find the roots of a quadratic equation, ax^2+ bx + c =0 . Consider the cases of both real and imaginary roots.
import cmath  #for handling complex nos
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d=b**2-4*a*c
if d>0:  #real roots
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print(f"The real and distinct roots are {r1} and {r2}")
elif d==0:
    r=-b/(2**a)
    print(f"The two equal roots are {r}")
else:
    r1=(-b+cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)
    print(f"The imaginary roots are {r1} and {r2}")


#Write a Python program to find distance between two points (x1,y1) and (x2,y2).
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)


#Write a Python program to check whether a number is Armstrong number or not.
number=int(input("Enter number:"))
Snumber=str(number)
no_digits=len(Snumber)
sum_power=0
temp=number
while temp>0:
    digit=temp%10
    sum_power+=digit**no_digits
    temp=temp//10
if number==sum_power:
    print("Armstrong")
else:
    print("Not Armstrong")
