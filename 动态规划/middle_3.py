# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
# 说明:
# 你可以认为每种硬币的数量是无限的。

"""
零钱兑换问题：初步一看 这个应该是贪心算法吧。但是既然在动态规划里，接着用动态规划做
完犊子了想不出传递方程，想出的传递方程都需要回溯；
当总金额为amount时，所需的最少硬币个数为dp[amount]，那么当amount = 11时，求出所有dp[1]、dp[2]、...、dp[11]的值。dp[1]到dp[10]就可以说是dp[11]的子问题，需要通过他们来求最终解。
以示例1为例，我们需要尽可能少的硬币个数，所以从11的总金额中取出任意一枚硬币，剩下的金额所需最少硬币个数再加上1就是所需硬币个数，即所需硬币个数为：dp[10]+1、dp[9]+1、dp[6]+1，再从中取最小值，即可求解。以此类推，dp[10]=min(dp[9]+1,dp[8]+1,dp[5]+1)...所以可以看出，通过求出所有dp[1]、dp[2]、...、dp[10]的值，最终就能得到dp[11]的值。

自己的思路：f(11) = min(f(10) + 1, f(9) + 1, f(6) + 1)
            f(10) = min(f(9) + 1, f(8) + 1, f(5) + 1)
所以传递方程：
            f(n) = min(f(n-1) + 1, f(n-2) + 1, f(n-5) + 1)
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()  # 给硬币从小到大排序
        dp = {0: 0}  # 生成字典dp，并且当总金额为0时，最少硬币个数为0
        for i in range(1, amount + 1):
            dp[i] = amount + 1  # 因为硬币个数不可能大于amount，所以赋值amount + 1便于比较
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i-j]+1)
        if dp[amount] == amount + 1:  # 当最小硬币个数为初始值时，代表不存在硬币组合能构成此金额
            return -1
        else:
            return dp[amount]
