
i,j=map(int,input().split())
a= [2**i for i in range(i,j+1) if i]
a.pop(1)
a.pop(-2)
print(a)
