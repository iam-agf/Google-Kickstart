t=int(input())
def solve(T):
    n,k=list(map(int,input().split()))
    array=list(map(int,input().split())) 
    sol=0
    counter=k
    for i in range(len(array)):
        if array[i]==counter:
            counter-=1
            if counter==0:
                sol+=1
                counter=k
        else:
            counter=k
            if array[i]==counter:
                counter-=1
                if counter==0:
                    sol+=1
                    counter=k
    print("Case #{}: {}".format(T,sol))

for tc in range(1,t+1):
    solve(tc)

# 3  Inputing the values n,k
# 4  Array of values to check
# 5  Our solution counter
# 6  A tracker to count if the number goes until k.
# 7  Start the main loop.
#    8  If the element being checked is equal to the counter, we can 
#       try to chain this element to a K-countdown.
#       9  And if that happens, we need our countdown to reduce 1 for the next
#          element.
#       10 If we achieve the counter to get until zero
#          11 We found one K-countdown array, so we add 1 to our solution 
#             counter.
#          12 And we must reset our counter in order to find the next 
#             K-countdown
#    13 Else 
#       14 the counter must be reset again to restart looking for another K-count
#          down
#       15 but since this element we're checking in this loop-step could be the 
#          beginning of a K-countdown, we apply the same process like in 8-12
#          16 Equal to 9
#          17 Equal to 10
#             18 Equal to 11
#             19 Equal to 12
# 21 Finish everything.