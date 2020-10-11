import numpy as np

class Solution:
	def probabilityOfHeads(self, prob, target):
		dp = np.zeros((len(prob)+1))
		dp[1] = prob[0]
		dp[0] = 1 - prob[0]
		for i in range(1, len(prob)):
			new_dp = np.zeros((len(prob)+1))
			for j in range(target+1):
				new_dp[j] = dp[j] * (1-prob[i]) + dp[j-1]*prob[i]
			dp = new_dp
		return dp[target]








#============================================================
prob = [0.4]
target = 1


sol = Solution()
ans = sol.probabilityOfHeads(prob, target)
print('prob = {}, target = {}'.format(prob, target))
print('ans = {}'.format(ans))

prob = [0.5, 0.5, 0.5, 0.5, 0.5]
target = 0
ans = sol.probabilityOfHeads(prob, target)
print('prob = {}, target = {}'.format(prob, target))
print('ans = {}'.format(ans))