def climbStairs( n):
    if n <= 3:
        return n #edike 3 er moddhe hole n return korbe karon calculation e etai ashe
    else:
        n1, n2 = 2, 3
        for i in range(4, n + 1):
            temp = n1 + n2  #loop ghure 4 theka n+1 bar and increment kore
            n1 = n2
            n2 = temp
        return n2
print(climbStairs(5))




def minCostClimbingStairs(cost):
    cost.append(0) #calculation er jonno
    for i in range(len(cost) - 3, -1, -1):  # 1 no index ke acces korar jonno karon oidik theka optimal
        cost[i] += min(cost[i + 1], cost[i + 2]) #1 ta jump ar 2 ta jump er modde min ta nibe
    return min(cost[0], cost[1])