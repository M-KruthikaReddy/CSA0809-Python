n=int(input("Enter values:"))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
if n==0:
    print("The number is palindrome.")
elif n!=0:
    print("The number is not a palindrome.")

