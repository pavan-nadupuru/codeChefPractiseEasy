import itertools
for _ in range(int(input())):
    found = False
    l=[]
    n,m = map(int,input().split())
    for __ in range(n):
        l.append(int(input()))

    for i in range(1,len(l)+1):
        if(found):
            break
        allp = list(itertools.combinations(l,i))
        for j in allp:
            if(sum(list(j)) == m):
                print("Yes")
                found = True
            if(found):
                break
    if(not found):
        print("No")