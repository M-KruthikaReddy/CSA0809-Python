n=int(input("Enter limit:"))
m={}
name=""
mob=0
i=0
for i in range (0,n):
    mob=int(input("Enter phone number:"))
    name=str(input("Enter name:"))
    z2=dict({mob:name})
    m.update(z2)
print(m)
n=int(input("Enter the num to search in dictionary: "))
print("The name of a person is" ,m[n])