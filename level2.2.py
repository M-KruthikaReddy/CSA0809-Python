matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n=len(matrix)
diagonal_elements=[]
diagonal_sum=0
for i in range(n):
    diagonal_elements.append(matrix[i][i])
    diagonal_sum+=matrix[i][i]
print("Diagonal elements are:",diagonal_elements)
print("Diagonal sum :",diagonal_sum)