def riverSizes(matrix):
    answer = []

    def check_river(i, j, current_river=0):
        if matrix[i][j] == 1:
            current_river += 1
            matrix[i][j] = 0
            # print "River at {},{}. Size {}".format(i,j,current_river)
            if i+1 < len(matrix):
                current_river = check_river(i + 1, j, current_river)
            if j+1 < len(matrix[i]):
                current_river = check_river(i, j + 1, current_river)
            if i-1 >= 0:
                current_river = check_river(i - 1, j, current_river)
            if j-1 >= 0:
                current_river = check_river(i, j - 1, current_river)
        return current_river

    # Write your code here.

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 1:
                answer.append(check_river(i, j))
    return answer

mtr=[
    [0,1,1,1,0],
    [1,1,0,0,1],
]
print(riverSizes(mtr))