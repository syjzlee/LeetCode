# https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/261/before-you-start/1106/

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4


"""
异或运算，相同的数字异或运算为0，  与0异或运算结果为其本身。
这题可以上升到求唯一的那个奇数次出现的数字。

大众思路是先排序，然后比较前后是否一样。
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            num = num ^ i
        return num



