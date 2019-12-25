# Longest Increasing Subsequence
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

"""
传递方程，f(i)表示以第i个元素结尾的最长上升序列的长度为f(i),最后求max(f(0)```f(n))即可。
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        result = [1 for _ in nums]
        max = nums[0]
        for i in range(1,len(nums)):
            maxlen = -1
            for j in range(0, i):
                if nums[i] > nums[j] and maxlen < result[j]:
                    maxlen = result[j]
            if maxlen >= 1:  # 说明之前的递增序列中，有ax可以跟的
                result[i] = maxlen + 1
            else:
                result[i] = 1
        return max(result)

# 这边有个优化成nlogn的图解。
# https://blog.csdn.net/u012505432/article/details/52228945
