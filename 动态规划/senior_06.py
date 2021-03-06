# 戳气球
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量。
#
# 说明:
#
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 示例:
#
# 输入: [3,1,5,8]
# 输出: 167
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


"""
状态转移方程：
预处理 nums = [1] + nums + [1], 给原数组首尾添加1, 并设新的数组大小为n
状态dp[i][j] 表示删除nums[i+1,..., j-1]之后的最大值，我们的目标是求dp[0][n-1]
状态转移方程 dp[i][j] = max{dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]}, i+1 <= k <= j-1
填充dp的方式，反斜三角
初始化 d[i][i+2] = nums[i] * nums[i+1] * nums[i+2]
"""


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for step in range(2, n):
            for i in range(n):
                if step == 2:
                    if i + step < n:
                        dp[i][i + step] = nums[i] * nums[i + 1] * nums[i + 2]
                        # print(i, i + step, dp[i][i+step])
                    continue
                for k in range(i + 1, i + step):
                    if i + step < n:
                        dp[i][i + step] = max(dp[i][k] + dp[k][i + step] + nums[i] * nums[k] * nums[i + step],
                                              dp[i][i + step])
                        # print(i, i + step, dp[i][i+step])
        return dp[0][n - 1]