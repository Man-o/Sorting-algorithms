l=[1,3,2,-3,5,7,6]
for ind1 in range(len(l)-1,0,-1):
    for ind2 in range(ind1):
        if l[ind2]<l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)
