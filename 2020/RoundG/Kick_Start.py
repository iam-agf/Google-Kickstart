from collections import OrderedDict
from math import ceil
t= int(input())

def solve(T):    
    string = input()
    solution = 0
    beginning = 0
    for i in range(4,len(string)+1):
        if string[i-4:i]=='KICK': beginning+=1
        if string[i-5:i]=='START' and i>5: solution += beginning
    print("Case #{}: {}".format(T,solution))


for i in range(1,t+1):
    solve(i)