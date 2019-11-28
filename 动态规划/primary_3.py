# 最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。



# 要理解这句话，以第i个数结尾的最大连续子数组。。。。！！！！
'''
求整个数组的最大和连续子数组，我们分解成n规模的问题dp，dp[i]表示以第i个数结尾的最大连续子数组。
因为dp[i]要求是必须以A[i]结尾的连续序列，那么只有两种情况：
1.这个最大和的连续序列只有一个元素，以A[i]开始，A[i]结尾
2.这个最大和的连续序列多个元素，从前面A[p]开始（p<i),一直到A[i]结束。
对于第一种情况，最大和就是A[i]本身。 第二张，最大和是dp[i-1]+A[i]。
于是得到方程：dp[i]=max(dp[i-1]+A[i],A[i])。 边界dp[0]=0.
'''

class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums[0]
        result = [_ for _ in nums]
        for i in range(1, len(nums)):
            result[i] = max(result[i - 1] + nums[i], nums[i])

        max_num = result[0]
        for i in result:
            if max_num < i:
                max_num = i
        return max_num

