#  to find all pairs in alist whose xor is equal to given target


def xor(l):
    l2=[]
    target=int(input("enter the target:"))
    for i in l:
        for j in l:
            if i^j==target:
                l2.append((i,j))

    print(l2)
xor([1,2,3,4,5,6])
