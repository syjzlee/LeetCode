# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]

# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。我们可以不考虑输出结果的顺序。

# 进阶:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
import collections

class Solution :
    def intersect(self, nums1, nums2):
        # 111111111111111111
        # len1, len2 = len(nums1), len(nums2)
        # if len1 == len2: len1+=1
        # dic = {len1:nums1, len2:nums2}
        # nums1_dic = {}
        # for i in dic[max(len1,len2)]:
        #     if i in nums1_dic:
        #         nums1_dic[i]+=1
        #     else:
        #         nums1_dic[i] = 1
        #
        # result = []
        # for i in dic[min(len1,len2)]:
        #     if i in nums1_dic:
        #         if nums1_dic[i] >= 1:
        #             nums1_dic[i]-=1
        #             result.append(i)
        # return result

        # 22222222222222222222222222222   真是日了狗的美观。
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())


solution = Solution()
print(solution.intersect(nums1 = [1,2], nums2 = [1,1]))