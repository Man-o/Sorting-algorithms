l=[3,1,-4,0,8,2]
for ind1 in range(len(l)-1):
    least=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[least]>l[ind2]:
            least=ind2
    l[ind1],l[least]=l[least],l[ind1]
print(l)
