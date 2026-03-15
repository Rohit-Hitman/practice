# # Group Words by Their Length

from collections import defaultdict

l=['apple1','apple2',"banana1", "kiwi", "apple3","kiwi"]

r=defaultdict(list)

for i in l:
    r[len(i)].append(i)
print("Group Words by Their Length : ",r)

# group by first char
r1=defaultdict(list)
for i in l:
    r1[i[0]].append(i)
print("group by first char : ", r1)

