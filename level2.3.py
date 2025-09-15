num=int(input("Enter number:"))
sum_of_divisors=0
for i in range(1,num):
    if num%i==0:
        sum_of_divisors+=i
if sum_of_divisors==num:
    print("It is a perfect number:")
else:
    print("It is not a perfect number:")