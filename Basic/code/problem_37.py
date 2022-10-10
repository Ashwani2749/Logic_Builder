# Write a program to print the first 10 Fibonacci numbers without recursion
# Solved By Ashwani2749

a=int(input("Enter the first number of series "))
b=int(input("Enter the second number of series "))
n=int(input("Enter the number of terms you want to get displayed "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
