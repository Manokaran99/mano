# mano
N,Q=input().split()
N,Q=int(N),int(Q)
k=input().split()
l=[]
for i in range(0,Q):
    s=input().split()
    l.append(s)
for i in range(0,Q):
    o=[]
    count=0
    for j in range(int(l[i][o])-1,int(l[i][l])):
        o.append(k[j])
        count+=int(k[j])
        print(count)
