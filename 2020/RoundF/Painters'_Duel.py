from collections import OrderedDict
t= int(input())

def solve(T):    
    N,X = list(map(int,input().split()))
    def mes(n):
        k=n//X
        if n-k*X>0:
            return k+1
        return k
    Q = list(map(int,input().split()))
    QQ = {i+1:Q[i] for i in range(len(Q))}
    QQQ = OrderedDict(sorted(QQ.items(), key=lambda t: mes(t[1])))
    solution = ' '.join(list(map(str,list(QQQ.keys()))))
    print("Case #{}: {}".format(T,solution))


for i in range(1,t+1):
    solve(i)