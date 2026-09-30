
e=[]
thi=[]
kl=int(input("enter the number of tuples:"))
for i in range(kl):
    q=int(input("enter1:"))
    thi.append(q)
    w=int(input("enter2:"))
    thi.append(w)
    e.append((q,w))
thi.sort()
v=thi[-1]+1



m=[[0]*v for _ in range(v)]
for u,p in e:
    m[u][p]=1
    m[p][u]=1
for i in m:
    for j in i:
        if j!=0 and j!=i[-1]:
            print(i)
        elif j!=0 and j==i[-1]:
            print(i)
adj=[[] for _ in range(v)]
for j,k in e:
    adj[j].append(k)
    adj[k].append(j)
for i in adj:
    if i!=[]:
        print(i)

