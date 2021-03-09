#Python3 

t=int(input()) 

def solve(T):
    n,d=list(map(int,input().split()))
    a=list(map(int,input().split()))
    sol=(d//a[n-1])*a[n-1]
    for i in range(n-2,-1,-1):
        if a[i+1]%a[i]==0: continue
        else:
            sol=(sol//a[i])*a[i]
    print("Case #{}: {}".format(T,sol))

for test_case in range(1,t+1):
    solve(test_case)

# Explanation of code

# 3  Receiving the number of cases 
# 5  Defining the main function 
    # 6  Receiving the values n,d from a list obtained from mapping the input splitted into integers.
    # 7  The list of values splitted and mapped into a list 
    # 8  First candidate of solution obtained from getting the LAST element of the array a and
    #    getting the integer division of the limit day multiplied by the last element
    # 9  Iteration in a reversed way throught the array from n-2 to 0.
        # 10 If the value I'm checking divides the last checked element in the array, I won't do anything
        # 11 Else, I will have to update my solution 
            # 12 like the first one, but having as limit day the last solution candidate
    # 13 Print the solution in the format required
# 15 Loop for all the test cases
# 16 iteration to solve each problem.
