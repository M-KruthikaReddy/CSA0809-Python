def find_repeat(lst):
    repeated=[]
    for i in lst:
        if lst.count(i)>1 and  i not in repeated:
            repeated.append(i)
        return repeated
number=[1,2,2,3,3,2,3,1,1,5,4]
print("Repeated elements:",find_repeat(number))
