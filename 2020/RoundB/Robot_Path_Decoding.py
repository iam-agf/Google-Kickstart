#Python3 

from operator import mul
from functools import reduce 
t=int(input())
d={'N':-1,'S':1,'E':1,"W":-1}
nums=set([str(i) for i in range(10)])
def solve(T):
    sol=[1,1]
    a=list(input())
    mults=[1]
    while len(a)!=0:
        mult=reduce(mul, mults, 1)
        n=a.pop(0)
        if n=='N' or n=='S': sol[1]+=d[n]*mult
        if n=='E' or n=='W': sol[0]+=d[n]*mult
        if n in nums:
            mults.append(int(n))
            a.pop(0)
        if n==')': mults.pop(-1)
    if sol[0]<1:
        if sol[0]==0: sol[0]=1000000000    
        else: sol[0]=sol[0]%1000000000
    if sol[1]<1:
        if sol[1]==0: sol[1]=1000000000    
        else: sol[1]=sol[1]%1000000000
    print("Case #{}: {} {}".format(T,sol[0], sol[1]))

for test_case in range(1,t+1):
    solve(test_case)

# Explanation of the code

# 3  imports multiply function to operate over a list with reduce (in 13). 
# 4  imports reduce to get the product of all a list (in 13)
# 5  Receiving the number of test cases to check 
# 6  Since we will move depending on those letters, we must translate each word to what it means
#    in terms of movement.
# 7  Set from 1 to 9 to verify if something is a number when we're iterating through the
#    array. It's a set because sets are optimized in Python to find elements inside them. 
# 8  Main Function
    # 9  We set sol=[1,1] because it's the first possible answer.
    # 10 Receiving the case input and changing it into a list.
    # 11 List that will be used as a stack to track the multipliers operating each moment.
    # 12 Main iteration until check all the list
        # 13 Each time the while occurs multiply content in the stack to apply this number of repetitions 
        #    over the next order that will appear. This is possible since the movements are commutative
        # 14 Poping from the list the next order
        # 15 If n is N or S, it affects the second coordinate, so we sum the order a $mul number of times.
        # 16 If is W or E, it will affect the first coordinate, so we sum the order a $mul number of times.
        # 17 If n is a (char that shows a) number, 
            # 18 we need to add it to our multipliers to apply it over the next orders
            # 19 and we pop the next element in the list because it will be a "(" that only gets in the way. 
        # 20 If n is ")", this mean that a pack of orders ended and we must delete the last element in our
        #    stack to stop multiplying by it in the next orders.
    # 21 In the end, the final thing we must verify is that the output we are considering is between 1 and 10**9
    #    so if the first coordinate it's a negative number OR ZERO:
        # 22 If it's zero, we must change it to 10**9
        # 23 Else just use mod 10**9
    # 24 the same as in the line 21, but for the second coordinate.
        # 25 If it's zero, we must change it to 10**9
        # 26 Else just use mod 10**9
    # 27 We just print the solution and finish
# 29 Loop to pass through all the test cases (remember it starts in 1 and ends in t+1
#    because python starts range from 0 to t-1)
# 30 Function that solves each case.