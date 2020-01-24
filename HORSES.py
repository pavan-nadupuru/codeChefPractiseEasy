import itertools
for _ in range(int(input())):
    n = input()
    mini = 0
    l = list(map(int,input().split()))
    l.sort()
    diffs=[]
    for k in range(len(l)-1):
        diffs.append(abs(l[k]-l[k+1]))
    print(min(diffs))

