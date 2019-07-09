# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数

class Solution :
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 利用冒泡法，但是时间复杂度太高了
        # for i in range(len(nums)):
        #     for j in range(len(nums)-i-1):
        #         if nums[j] == 0:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]

        # 利用空间一次性交换,非0放前面，0最后放入
        # k = 0
        # for i in nums:
        #     if i != 0:
        #         nums[k] = i
        #         k+=1
        # for i in range(k,len(nums)):
        #     nums[i] = 0

        # 同时考虑非0和0.
        k = 0
        for i,value in enumerate(nums):
            if value != 0 and i!=k:
                nums[k], nums[i] = nums[i], nums[k]
                k+=1

        return nums

solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))




