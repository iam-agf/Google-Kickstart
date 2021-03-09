#Python3

t=int(input())
def solve(T):
    sol=0 
    x=int(input()) 
    a=list(map(int,input().split())) 
    for i in range(1,x-1): 
        if a[i]>a[i-1] and a[i]>a[i+1]: 
            sol+=1 
    print("Case #{}: {}".format(T,sol)) 

for test_case in range(1,t+1):
    solve(test_case)


# Explanation of code

# 3  Input the number of test cases
# 4  Start of te main function that solves the problem
    # 5  Set the solution to 0 (we don't know more about it)
    # 6  Receive the size of the next input
    # 7  Receiving the input and splitting it into a list to use them properly 
    # 8  iterate from the second element to the n-1 element (FIRST AND LAST CAN'T BE PEAKS)
        # 9  and check if it's greater that its neighbours.
            # 10 If it does sum 1 to the final solution.
    # 11 Finishing the loop, print the answer with the appropiate format.
# 13 Loop to iterate through all the test cases.
    # 14 For each case we do operate over it with solve