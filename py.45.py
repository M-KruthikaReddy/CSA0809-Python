def repeated(arr):
    repeated=[]
    for i in arr:
        if arr.count(i)>1 and i not in repeated:
            repeated.append(i)
            return repeated
arr=[1,2,3,2,4,5,1,6]
print("Repeated elements:",repeated(arr))