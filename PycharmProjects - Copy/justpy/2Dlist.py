matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# 3x3 metrics (2 Dimention list)
matrix [0] [1] = 20
print (matrix [0][1])
print (matrix)
print (matrix[0])
# nested loops to iterate over the items in matrix

for row in matrix:
    for item in row:
        print (item)

