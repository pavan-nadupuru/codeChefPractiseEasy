a,b=input().split()
ans=str(int(a)-int(b))
if(len(ans)==1):
    print(3 if ans != '3' else 4)
else:
    print('7'+ans[1:] if('7'+ans[1:] != ans) else '6'+ans[1:])