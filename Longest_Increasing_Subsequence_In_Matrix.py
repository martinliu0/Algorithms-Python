#Based on the problem and solution of the following link:
#   http://stackoverflow.com/questions/6558710/longest-increasing-sequence-2d-matrix-recursion
#I was initially confused about going backwards in the graph, i.e. going from matrix[i][j] to matrix[i-1][j]
#hence the commented section in find_lis(_,_)


matrix = [[97,47,56,36,60,31,57,54,12,55],
[35,57,41,13,82,80,71,93,31,62],
[89,36,98,75,91,46,95,53,37,99],
[25,45,26,17,15,82,80,73,96,17],
[75,22,63,96,96,36,64,31,99,86],
[12,80,42,74,54,14,93,17,14,55],
[14,15,20,71,34,50,22,60,32,41],
[90,69,44,52,54,73,20,12,55,52],
[39,33,25,31,76,45,44,84,90,52],
[94,35,55,24,41,63,87,93,79,24]]
longest = []

def lis():
    global longest
    global matrix
    longest = [len(i)*[0] for i in matrix]
    maxval = 0
    for i in range(0, 2):
        for j in range(0, 1):
            curr = find_lis(i,j)
            maxval = curr if curr > maxval else maxval
    print(longest)
    return maxval

def find_lis(i, j):

    if longest[i][j] == 0:
        maxval = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if not (k == 0 and l ==0) and i + k >= 0 and i + k < len(matrix) and j + l >= 0 and j + l < len(matrix[0]) and matrix[i][j] > matrix[i+k][j+l]:
                    curr = find_lis(i + k, j+ l)

                    maxval = curr if curr > maxval else maxval

        #use this code instead if the path cannot go backwards
        #maxval = 0
        # if curr1 != 0:
        #     curr1 = curr1 if matrix[i-1][j] < matrix[i][j] else 0
        #
        # curr2 = find_lis(i, j-1) if j-1 >= 0 else 0
        #
        # if curr2 != 0:
        #     curr2 = curr2 if matrix[i][j-1] < matrix[i][j] else 0
        #
        # curr3 = find_lis(i-1, j-1) if i-1 >= 0 and j -1 >= 0 else 0
        # if curr3 != 0:
        #     curr3 = curr3 if matrix[i-1][j-1] < matrix[i][j] else 0



        longest[i][j] = maxval + 1

    return longest[i][j]

if __name__ == "__main__":
    print(lis())
