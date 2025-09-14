num=int(input("Enter number:"))
sum_digit=0
temp=num
while temp>0:
    digit=temp%10
    sum_digit+=digit**3
    temp//=10
if num==sum_digit:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")