def conq(l,left,right):
    lind,rind,mind=0,0,0
    while lind<len(left) and rind<len(right):
        if left[lind]>right[rind]:
            l[mind]=right[rind]
            rind+=1
        else:
            l[mind]=left[lind]
            lind+=1
        mind+=1
    while lind<len(left):
        l[mind]=left[lind]
        lind+=1
        mind+=1
    while rind<len(right):
        l[mind]=right[rind]
        rind+=1
        mind+=1
def divid(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        divid(left)
        divid(right)
        conq(l,left,right)
l=[5,3,1,7,9,2]
divid(l)
print(l)
