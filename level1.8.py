import statistics
arr=[12,45,82,53]
mean=statistics.mean(arr)
median= statistics.median(arr)
mode=statistics.mode(arr)
avg=(mean+median+mode)/3
print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)
print("Avg of mean,median,mode:",int(avg))