for _ in range(int(input())):
    totalDishes, compDishes = input().split()
    completedDishes = list(map(int,input().split()))
    chef, chefAssis,toAssis = [],[],False
    for i in range(1,int(totalDishes)+1):
        if(i not in completedDishes):
            if(toAssis):
                chefAssis.append(str(i))
                toAssis = False
            else:
                toAssis = True
                chef.append(str(i))
    print(' '.join(chef))
    print(' '.join(chefAssis))

