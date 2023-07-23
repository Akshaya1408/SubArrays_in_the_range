def subarray(a,b,c):
    res=[]
    for i in range(b,c+1):
        res.append(a[i])
    return res

a=list(map(int,input().split()))
b=int(input())
c=int(input())
print(subarray(a,b,c))