arr=[14,16,87,36,25,89,34]
M=1
N=3
arr.sort()
Mth_max=arr[-M]
Nth_min=arr[N-1]
sum=Mth_max+Nth_min
diff=Mth_max-Nth_min
print("1st max num:",Mth_max)
print("3rd min num:",Nth_min)
print("Sum:",sum)
print("Diff:",diff)