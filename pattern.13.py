n=5
num=1
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(num,i+1):
        print(" "*(n-i),end=" ")
        num+=1
    print()
    for i in range(n,0,-1):
     print(" "*(n-i),end=" ")
     for j in range(num,i+1):
          print(" "*(n-i),end=" ")
          num+=1
          print()
    