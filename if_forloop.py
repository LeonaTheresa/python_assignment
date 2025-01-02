#1.check whether the input character is a vowel,consonant,digit or speccial character
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


#2.sum of first n numbers
n = int(input("Enter value for n: "))  
s=0 
for i in range(1,n+1):
    s = s+i
print("Sum is ",s)


#3.Print Odd Numbers from l down to 1 in Reverse
l = int(input("Enter value for l: ")) 
if l%2==0:
    l=l-1
for i in range(l,0,-2):
    print(i,end=" ")



#4.Write the python program to print all prime numbers less than 1000.
for n in range(2, 1000):
    is_prime = True  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            is_prime = False
            break  
    if is_prime:
        print(n)


            

#5.Write a python program to find out the eldest and youngest of three individuals ,with their ages being input through the keyboard.(without using max, min functions)
age1=int(input("Enter age1"))
age2=int(input("Enter age2"))
age3=int(input("Enter age3"))
if age1>age2 and age1>age3:
    print("Eldest is ",age1)
elif age2>age1 and age2>age3:
    print("Eldest is ",age2)
else:
     print("Eldest is ",age3)
if age1<age2 and age1<age3:
    print("Youngest is ",age1)
elif age2<age1 and age2<age3:
    print("Youngest is ",age2)
else:
     print("Youngest is ",age3)


#6.Write a python program to print factorial of a given number.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
        factorial *= i
print(f"The factorial of {num} is {factorial}")


#7. Write a python program to find X^Y or pow(x,y) without using standard function
x = int(input("Enter x: "))
y = int(input("Enter y: "))
result = 1
for _ in range(y):  
    result *= x
print(f"Result is {result}")


#8.Write a program that accepts the lengths of three sides of a triangle as inputs andoutputs whether or not the triangle is a right triangle.
side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3(largest side): "))
if side1**2 + side2**2 == side3**2:
    print("It is right triangle")
else:
    print("It is not right triangle")




#9.Write a Python program to display the sum of odd numbers between a programmer specified upper and lower limit.
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
sum_of_odds = 0
for num in range(lower_limit, upper_limit + 1):
    if num % 2 != 0: 
        sum_of_odds += num  
print(f"The sum of odd numbers between {lower_limit} and {upper_limit} is: {sum_of_odds}")


#10.Print Odd Numbers from l down to 1 in Reverse
l = int(input("Enter value for l: ")) 
if l%2==0:
    l=l-1
for i in range(l,0,-2):
    print(i,end=" ")
