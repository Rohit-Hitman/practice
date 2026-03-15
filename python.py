##find top 3 product sale 

l=["p1","p2","p4","p4","p3","p3","p2","p4","p3","p5","p5","p5","p5","p5","p5","p5","p6","p4"]

d={}
for i in l:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
# print(d)
d1=sorted(d.items(), key=lambda x:x[1], reverse=True)

d2=dict(d1[:3])
print(d2)
c=0
for i,j in d2.items():
    print(c,"",i,": ", j)
    c=c+1

 
