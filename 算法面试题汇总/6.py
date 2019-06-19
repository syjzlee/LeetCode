# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# 典型回溯法，solution2 的写法更舒服点。

# 学习到的
# nums = [1,2,3,4,5,6]
# a,*i,b = nums
# >>>*i
# [2,3,4,5]

class solution1:
    def _partition(self, s):
        if not s:
            return []
        result = []
        self._partition(s, [], result)
        return result

    def _partition(self, s, base, result):
        for i in range(1,len(s) + 1):
            if all([s[:i] == s[:i][::-1], s[:i]]):
                base.append(s[:i])
                new_s = s[i:]
                if new_s:
                    self._partition(new_s, base, result)
                else:
                    result.append(base.copy())
                base.pop()


class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        result = []
        if len(s) == 1:
            return [[s]]
        self._partition(s, 0, [], result)
        return result

    def _partition(self, s, start, base, result):
        if start == len(s):
            result.append(base.copy())

        for i in range(start, len(s) + 1):
            if s[start:i] == s[start:i][::-1] and s[start:i]:
                base.append(s[start:i])
                self._partition(s, i, base, result)
                base.pop()

