# 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
#
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。


#  https://blog.csdn.net/weixin_42095500/article/details/83027749
#  好吧 这个状态转移方程最开始竟然没想出来。。。。。。看了这个通俗了很多，高中求函数的功夫都忘记了。。。。

"""
下一规模的解，也就是memo[n]，要么是memo[n-1] （不偷，保持原状），或是memo[n-2]+nums[n]（放弃上一家，偷这家）。
由于程序不知道上一家有没有偷，我们两个选择都算一下，取较大值即可。

这句话要这么理解。  这个不偷就是确定指当前第I家的不偷，所以它的最大解就是前面i-1家的最大解，而如果这一家偷了所以就要加上
前面i-2家的最大解， 你不用关心i-1家时候到底第i-1家是否被偷了，只比较这两个值就完全是充分必要条件。当前转移方程关注的是第i家。
"""

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = [_ for _ in nums]
        result[1] = max(nums[:2])
        for i in range(2,len(nums)):
            result[i] = max(result[i-1], result[i-2]+nums[i])

        return result[-1]
