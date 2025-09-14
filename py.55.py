n=int(input("Enter number:"))
s=str(n)
if len(s)%2==0:
    half=len(s)//2
    first= int(s[:half])
    second=int(s[half:])
    if (first+second)**2==n:
        print("Tech num")
    else:
        print("Not a tech num")