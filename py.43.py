a=()
l=[]
n=int(input("Enter values:"))
for i in range (0,n):
    items=int(input("enter elements:"))
    l.append(items)
a=a+tuple(l)
print("tuple is",a)