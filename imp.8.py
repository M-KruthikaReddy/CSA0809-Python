import math
def is_perfect_square(n):
    root=int(math.sqrt(n))
    return root*root==n
numbers=[4,7]
for num in numbers:
    print(num,"->",is_perfect_square(num))