'''1.Consider the mathematical expression (a+b)^2=a^2+2ab+b^2. Write a Python
program that takes user input for values of a and b, then evaluates both sides of
the expression. Finally, compare the results and print whether the equation holds
true or false.   (UQ-MAY 2024)'''  

a =int(input("Enter the value of a: "))
b =int(input("Enter the value of b: "))
lhs = (a + b)**2  
rhs = a**2 + 2*a*b + b**2  
if lhs == rhs:
    print("The equation holds true.")
else:
    print("The equation does not hold true.")


#2.Write a Python program to print all prime factors of a given number.(UQ-JAN 2024)
n = int(input("Enter a number: "))
print("Prime factors of", n, "are:")

for i in range(2, n + 1):
    is_prime = True  
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and n % i == 0:
        print(i, end=" ")





'''Write a python program to generate the following type of pattern for the given N
rows .
1 2 3 4
1 2 3 
1 2 
1
'''
n=int(input("Enter no of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

