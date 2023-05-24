def revprint(*a, **b): 
    print(*reversed(a), **b) 
 
revprint(10, 20, 30, 40, 50, sep=',')