# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#0
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false

class Solution :
    def increasingTriplet(self, nums) -> bool:
        ans = [float('inf'), float('inf')]
        for i in nums:
            if i > ans[1]:
                return True
            elif i <= ans[0]:
                ans[0] = i
            else:
                ans[1] = i
        return False

solution = Solution()
print(solution.increasingTriplet([1,2,3,4,5]))


"""
求最长递增子序列。 动态规划
"""
class myStack:
    #找出以元素i结尾的最长递增子序列
    #每一次为ｉ进行分配时，要检查前面所有的算法ai(i<x)
    #若ai小于ax，则说明ax可以跟在ai后形成一个新的递增子序列
    #否则，以ax结尾的递增子序列的最长长度为1
    def getHeight(self, men, n):
        longest = {}    #c存一个字典
        longest[0] = 1
        for i in range(1, len(men)):
            maxlen = -1
            for j in range(0, i):
                if men[i]>men[j] and maxlen<longest[j]:
                    maxlen = longest[j]
            if maxlen>=1:    #说明之前的递增序列中，有ax可以跟的
                longest[i] = maxlen +1
            else:
                longest[i] = 1
        return max(longest.values())

