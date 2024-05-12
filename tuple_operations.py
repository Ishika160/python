x=(1,2,3,4,"hello") #create
print(x[3]) #update
l=list(x)

i=2
n=10
l[i]=n
updated_tuple=tuple(l)
print(updated_tuple)

id=3
del l[id]
print(l)