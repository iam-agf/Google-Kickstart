from collections import OrderedDict
from math import ceil
t= int(input())

def solve(T):    
    N,X = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    QQ = {i+1:Q[i] for i in range(len(Q))}
    QQQ = OrderedDict(sorted(QQ.items(), key=lambda t: ceil(t[1]/X)))
    solution = ' '.join(list(map(str,list(QQQ.keys()))))
    print("Case #{}: {}".format(T,solution))


for i in range(1,t+1):
    solve(i)