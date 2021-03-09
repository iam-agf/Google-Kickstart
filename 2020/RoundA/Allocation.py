t=int(input())
def solve(T):
    n,b=list(map(int,input().split())) 
    sol=0
    A=list(map(int,input().split()))
    A.sort()
    for i in range(n):
        if A[i]<=b:
            b-=A[i]
            sol+=1 
        else:
            break
    print("Case #{}: {}".format(T,sol))

for i in range(1,t+1):
    solve(i)

# Explanation of the code
# 
# 1  Receive of the number of test cases.
# 2  Main function to solve each case
    # 3  Inputting values n,b from list obtained from splitting the input.
    # 4  Setting sol where will be where we will save the number of possible bought houses.
    # 5  Splitting the input of the values of the houses into a list called A
    # 6  We sort A to use a Greedy Algorithm to achieve the max number of bought houses.
    # 7  We iterate from 0 to n-1 to check that list
        # 8  If the smallest non-bought house costs less than our budget, we buy it.
            # 9  We quit its value to the budget
            # 10 And we add 1 to the number of bought houses.
        # 11 Else this will mean the next houses will be more expensive than this we just
        #    check, so we can stop looking for houses to buy, and finish our iteration.
            # 12 with a break.
    # 13 Finally we print in the requested format.
# 14 Loop through all the cases.
# 15 Function to solve the case.