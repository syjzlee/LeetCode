# Perfect Squares
# # 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# #
# # 示例 1:
# #
# # 输入: n = 12
# # 输出: 3
# # 解释: 12 = 4 + 4 + 4.
# # 示例 2:
# #
# # 输入: n = 13
# # 输出: 2
# # 解释: 13 = 4 + 9.

"""
https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51584790
"""

import math

class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [i for i in range(n+1)]
        # for i in range(1, 4):            # 有个四平方定理。
        #     dp[i] = i
        for i in range(4, n + 1):
            max_n = int(math.sqrt(i))
            if max_n * max_n == i:
                dp[i] = 1
            else:
                for j in range(1, max_n + 1):
                    dp[i] = min(dp[i], dp[i - j * j] + dp[j * j])
                    # print(i, dp[i], "|", max_n, i, j)
        return dp[-1]


s = Solution()
print(s.numSquares(12))

