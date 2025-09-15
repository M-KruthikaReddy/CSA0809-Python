nums=[4,54,29,71,89,98,23]
prime_count=0
composite_count=0
for num in nums:
    if num <2:
        continue
    is_prime=True
    for i in range (2,int(num**0.5)+1):
        if num % i==0:
            is_prime=False
            break
    if is_prime:
        prime_count+=1
    else:
        composite_count+=1
print("Composite number:",composite_count)
print("Prime number:",prime_count)