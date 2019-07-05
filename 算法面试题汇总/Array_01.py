# 给定一个整数数组nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 示例
# 1:
# 输入: [2, 3, -2, 4]
# 输出: 6
# 解释: 子数组[2, 3]有最大乘积6。

# 示例
# 2:
# 输入: [-2, 0, -1]
# 输出: 0
# 解释: 结果不能为2, 因为[-2, -1]不是子数组。

"""
经典动态规划 自底向上
"""

class Solution:
    def maxProduct(self, nums) -> int:
        result = nums[0]
        maxDp = nums.copy() # 又忘记拷贝了。
        minDp = nums.copy()
        for i in range(1,len(nums)):
            tempmax = maxDp[i-1] * nums[i]
            tempmin = minDp[i-1] * nums[i]
            maxDp[i] = max(max(nums[i], tempmax), tempmin)
            minDp[i] = min(min(nums[i], tempmin), tempmax)
            result = max(result, maxDp[i])
        return result

solution = Solution()
print(solution.maxProduct([0,2]))

