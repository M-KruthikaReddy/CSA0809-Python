def is_lucky(n):
    num=list(range(1,n*2))
    step=2
    while step<=len(num):
        del num[step-1::step]
    step+=1
    return n in num
n=int(input("Enter number:"))
print("Lucky num"if is_lucky(n)else"not lucky")