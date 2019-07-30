n,q=input().split()
n,q=int(n),int(q)
K=input().split()
L=[]
for i in range(0,q):
    S=input().split()
    L.append(S)
for i in range(0,q):
    out=[]
    count=0
    for j in range(int(L[i][out])-1,int(L[i][L])):
        out.append(K[j])
        count+=int(K[j])
        print(count)
