# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if s == t:
            return True
        word_dict = {}
        for i in s:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1
        for i in t:
            if i in word_dict.keys() and word_dict[i] != 0:
                word_dict[i]-=1
            else:
                return False


# 吗的 别人的脑子怎么就能记住这个   我怎么老在造车轮 还是方的车轮
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        u = set(s)

        for v in u:
            if s.count(v) != t.count(v):
                return False

        return True


solution = Solution()
print(solution.isAnagram("anagram","nagaram"))