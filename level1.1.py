print("Enter -1 to exit,  enter the numbers: ")
positive_sum =0
positive_count=0
negative_sum=0
negative_count=0
while True:
    num=int(input())
    if num==-1:
        break
    elif num>0:
        positive_sum+=num
        positive_count+=1
    elif num<0:
        negative_sum+=num
        negative_count+=1
    if positive_count>0:
        avg_positive=positive_sum/positive_count
    else:
        avg_positive=0
    if negative_count>0:
        avg_negative=negative_sum/negative_count
    else:
        avg_negative=0
print("avg negative num is",int(avg_negative))
print("avg positive num is",int(avg_positive))