from operator import add

t= int(input())

def solve(T):    
    size = int(input())
    column_sums = [0]*(size)
    row_sums = [0]*(size)
    matrix = []

    for i in range(size):
        row = list(map(int,input().split()))
        matrix.append(row)

    for i in range(size):
        adding_row = matrix[i][i:]
        adding_row.extend([0]*i)

        adding_col = [0]*(size-i)
        adding_col.extend(matrix[i][:i])

        column_sums = list( map(add, column_sums, adding_row ))
        row_sums = list( map(add, row_sums, adding_col ))

    sol = max(max(column_sums), max(row_sums))
    print("Case #{}: {}".format(T,sol))


for i in range(1,t+1):
    solve(i)