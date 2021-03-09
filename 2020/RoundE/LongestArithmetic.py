number_of_cases= int(input())

def solve(case):
    actual_maximal_length=0
    N=int(input())
    Ai=list(map(int,input().split()))
    arithmetic_difference=0
    actual_length=0
    for i in range(1,N):
        if arithmetic_difference==Ai[i-1]-Ai[i]:
            actual_length+=1
        else:
            arithmetic_difference=Ai[i-1]-Ai[i]
            if actual_maximal_length < actual_length: 
                actual_maximal_length = actual_length
            actual_length=1
    if actual_maximal_length< actual_length:
        actual_maximal_length = actual_length
                
    print("Case #{}: {}".format(case,actual_maximal_length+1))


for i in range(1,number_of_cases+1):
    solve(i)