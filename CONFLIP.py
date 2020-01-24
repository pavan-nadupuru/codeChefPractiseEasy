for _ in range(int(input())):
    for __ in range(int(input())):
        i,n,q = map(int,input().split())
        if(i==q):
            ans = n
        else:
            ans =0
        ans = int(abs(ans - ((n+1)/2 if n%2==1 else n/2)))
        print(ans)
