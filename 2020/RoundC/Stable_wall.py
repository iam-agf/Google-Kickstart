t=int(input())

def solve(T):
    r,c=list(map(int,input().split()))
    R=[]
    for i in range(r):
        R.append(input())
    sol=[]
    for cc in range(c):
        stack=list()
        for rr in range(r):
            if R[rr][cc] in stack:
                if R[rr][cc]!=stack[-1]:
                    print("Case #{}: {}".format(T,-1))
                    return
            else:
                if R[rr][cc] not in sol:
                    if stack==[]:
                        sol.append(R[rr][cc])
                    else:
                            sol.insert(sol.index(stack[-1]),R[rr][cc])
                stack.append(R[rr][cc])
    print("Case #{}: {}".format(T,''.join(sol)))
    
for tc in range(1,t+1):
    solve(tc)

# 4  Input the number of rows and cols.
# 5  List to save the rows for next input
# 6  Loop to start saving
#    7  Actually adding the rows
# 8  List to save how are saved the pieces This is actually relevant
#    since the structure functions will help me correcting if I miss
#    adding a value that was before any other saved previously.
# 9  loop to check each column
#    10 Stack to see if structure is possible.
#    11 Loop to check each element in the column.
#        12  If the element in the row we're checking is already in the
#            stack, it MUST be equal to the last element added in that 
#            stack or you will have a hook-type structure that can't happen
#            13 if the structure is exactly the case described in 12
#                14 print that it's an impossible case
#                15 and finish this it
#        16  Else it means we can just add it to the stack 
#            17  but if it isn't already in the solution
#                18  it can be because the stack is empyt (start of 
#                    the checking)
#                    19 and we just add it. 
#                20  else
#                    21 just put the element before the index of the last
#                       stacked element.
#            22  and we just add the element checked to the stack for next ops
# 23 Then we just print the solution joining the list structure.