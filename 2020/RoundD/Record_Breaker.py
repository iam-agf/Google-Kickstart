t=int(input())

def output(test_case,solution):
    print("Case #{}: {}".format(test_case,solution))

def solve(number_case):
    days=int(input())
    visitors_per_day=list(map(int,input().split()))
    solution=0
    last_max=-1 # Max number of visitors from prev days.
    for i in range(days):
        if visitors_per_day[i]>last_max: 
            if i<days-1:
                if visitors_per_day[i]>visitors_per_day[i+1]: 
                    solution+=1
            else: 
                solution+=1
        if visitors_per_day[i]>last_max:
            last_max=visitors_per_day[i]
    output(number_case,solution)
    
for tc in range(1,t+1):
    solve(tc)