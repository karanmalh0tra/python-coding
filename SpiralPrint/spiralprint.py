#row right to left => col_start to col_end and then increment row_start by 1
#col top to bottom=> row_start to row_end and then decrement col_end by 1

#row left to right => col_end to col_start and then decrement row_end by 1
# col bottom to top => row_end to row_start and then increment col_start by 1


def spiralPrint(arr):
    count = 0
    m = len(arr[0])
    n = len(arr)
    row_start, col_start = 0,0
    row_end,col_end = n-1,m-1
    while(count < m*n):
        for i in range(col_start,col_end+1):
            print(arr[row_start][i], end = " ")
            count = count + 1
        row_start = row_start + 1
        for j in range(row_start,row_end+1):
            print(arr[j][col_end], end = " ")
            count = count + 1
        col_end = col_end - 1
        for k in range(col_end,col_start-1,-1):
            print(arr[row_end][k], end = " ")
            count = count + 1
        row_end = row_end - 1
        for l in range(row_end,row_start-1,-1):
            print(arr[l][col_start], end = " ")
            count = count + 1
        col_start = col_start + 1



#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)
