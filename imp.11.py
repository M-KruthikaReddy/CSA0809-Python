def find_index(lst,target):
    if target in lst:
        return lst.index(target)
    else:
        return-1
    numbers=[10,20,30,40,50]
    target=30
    print("Index of",target,"is:",find_index(numbers,target))
    