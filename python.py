# #we have two dictionary, id and values, combine values in one without duplicacy

d1={"id":[1,2,3]}
d2={"id":[3,10,5,4]}

d3=set(d1["id"]+d2["id"])
print(d3)
print(type(d3))

d4=(d1["id"]+d2["id"])
print(d4)
print(type(d4))

