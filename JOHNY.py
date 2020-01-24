for _ in range(int(input())):
    input()
    l=list(map(int,input().split()))
    ele = l[int(input())]
    l.sort()
    print(l.index(ele))

