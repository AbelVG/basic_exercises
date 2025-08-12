#A script that creates a pascal triangle with the input of how many rows to go down.
print("This script generates a pascal triangle")
rows = int(input("How many rows should your pascal triangle be? The minimum is 3: "))
if rows < 3:
    rows = 3

def pascalTriangle(rows):
    triangle = []
    level = 0
    for row in range(rows):

        triangle.append([])
        if level == 0:
            triangle[level].append(1)
        elif level == 1:
            triangle[level].extend([1, 1])
        else:
            triangle[level].append(1)
            prev = triangle[level-1]
            for j in range(1, len(prev)):
                triangle[level].append(prev[j-1]+prev[j])
            triangle[level].append(1)
        level += 1            


    return triangle

triangle = pascalTriangle(rows)

for row in triangle:
    print(row, "\n")