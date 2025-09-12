num=int(input("enter a value:"))
lim=int(num/2)+1
for i in range (2,lim):
    rem=num%i
    if rem==0:
        print(num,"is not a prime number")
    elif rem!=0:
        print(num,"is a prime number")
