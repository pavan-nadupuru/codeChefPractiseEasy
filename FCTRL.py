def calTrail(n):
    if(n//5 == 0):
        return 0
    else:
        return (n//5 + calTrail(n//5))


for _ in range(int(input())):
    n = int(input())
    print(calTrail(n))
