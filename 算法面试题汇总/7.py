# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

"""
傻瓜式的暴力解法。
"""
class Solution1:
    def wordBreak(self, s, wordDict):
        if not s:
            return False
        maxlen = 0
        for word in wordDict:
            if maxlen < len(word):
                maxlen = len(word)

        return self.wordsplit2(s, [0], 0, wordDict,maxlen)   # 1 . 2 分别是递归和非递归的暴力解法，  没法用。
        # return self.wordsplit1(s, [0], 0, wordDict,maxlen)

    def wordsplit(self, s, split_index, start, wordDict):
        if len(split_index) == 0:
            return False

        for i in range(start, len(s) + 1):
            if s[split_index[-1]:i] in wordDict:
                if i == len(s):
                    return True
                split_index.append(i)
                # print(s[split_index[-2]:i])
                return self.wordsplit(s, split_index, i, wordDict)
            elif i == len(s):
                start = split_index.pop()
                return self.wordsplit(s, split_index, start + 1, wordDict)

    def wordsplit2(self,s , split_index, start, wordDict, maxlen):
        i = 0
        while i <= len(s) + 1:
            if len(split_index) == 0:
                return False
            if s[split_index[-1]: i] in wordDict:
                split_index.append(i)
                # print(s[split_index[-2]: i])
            if (i - split_index[-1]) >= maxlen:
                print(split_index)
                i = split_index.pop()
            if i == len(s)+1 and s[split_index[-1]:i] in wordDict:
                return True
            i += 1


"""
在网页上提交代码，提示超过了做大的递归深度, 应该为动态规划的思想
用一个数组res来存状态，0代表以当前索引对应的字符为结尾的字符串不可被完全拆分，1代表可以拆分。
之后遍历字符串的每个字符，对于每个字符，用一个指针p向前找距离在maxlen以内的字符串，当满足以下两个条件，即说明以当前字符结尾的字符串是可以被拆分的：

p指向的位置的状态是1（说明0到p的字符串是可以完全拆分的），且s[p+1:i]在字典里面
p指向的位置的状态是字符串的开头，且s[p:i+1]在字典里面
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 求字典中最长字符串
        maxlen = 0
        for word in wordDict:
            if len(word) > maxlen:
                maxlen = len(word)

        res = [0] * len(s)
        for i in range(len(s)):
            p = i
            while (p >= 0 and i - p <= maxlen):
                # 两个条件
                if (res[p] == 1 and s[p + 1:i + 1] in wordDict) or (p == 0 and s[p:i + 1] in wordDict):
                    res[i] = 1
                    break
                p -= 1
            print(res)
        return res[-1]


solution = Solution()
if solution.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]):
    print(1)
else:
    print(2)
