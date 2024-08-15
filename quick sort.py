def quick(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[val for val in l[1:] if pivot>val]
    right=[val for val in l[1:] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
l=[4,2,9,51,1]
print(quick(l))
