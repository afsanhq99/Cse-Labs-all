
import math
def getZero(n):

	dp = [math.inf for i in range(n + 1)]
	dp[0] = 0
	for i in range(n + 1):
		for c in str(i):
			dp[i] = min(dp[i],dp[i - (ord(c) - 48)]+1)
	return dp[n]


N = 25
print(getZero(N))



