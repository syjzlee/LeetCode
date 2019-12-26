# 乘积最大子序列
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""
状态转移方程: 以第i个数结尾的序列中乘积最大的连续子序列乘积
有两种情况，当前数与之前相乘结果变大，当前数与之前相乘结果变小。
f(i) = max(nums[i],maxDp[n-1]*nums[i], minDp[n-1]*num[i])
tempmax = maxDp[i-1] * nums[i]
tempmin = minDp[i-1] * nums[i]
maxDp[i] = max(max(nums[i], tempmax), tempmin)
minDp[i] = min(min(nums[i], tempmin), tempmax)
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxDp = {0: nums[0]}
        minDp = {0: nums[0]}
        for i in range(1, len(nums)):
            tempmax = maxDp[i - 1] * nums[i]
            tempmin = minDp[i - 1] * nums[i]
            maxDp[i] = max(max(nums[i], tempmax), tempmin)
            minDp[i] = min(min(nums[i], tempmin), tempmax)
        return max(maxDp.values())