# 摩尔投票法，前提 ：：：：：  众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素

# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2


'''
厉害了，  摩尔投票法精髓啊。。。。。  重点是题目要求，众数是次数大于n/2的数
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        tmp = nums[0]
        for num in nums:
            if num == tmp:
                count+=1
            else:
                if count == 0:
                    tmp = num
                    continue
                count-=1
        return tmp