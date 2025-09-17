name=input("Enter name:")
mobile=input("Enter mobile num:")
cost=float(input("Enter cost :"))
if cost>1000:
    discount=cost*0.10
else:
    discount=cost*0.05
total=cost-discount
print("\n-----Bill-----")
print("Name:",name)
print("Mobile num:",mobile)
print("Cost:",cost)
print("Discount:",discount)
print("Total amount:",total)