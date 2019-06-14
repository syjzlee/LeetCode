# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
import string

# 个人评估， 1,2 时间一样，但是我认为开辟了额外的内存空间. 2相对更好. 3 看着就舒服。。。。。 时间最短，内存比2多点。
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        new_s = ''
        for i in s:
            if i.isalpha() or i.isalnum():
                new_s += i
        mid = int(len(new_s)/2)
        s = new_s.lower()
        if mid > 0:
            for i in range(mid):
                if s[i] != s[-1-i]:
                    return False
            return True
        else:
            return True

    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        if len(s) == 0: return True
        head ,tail = 0,len(s)-1
        while head < tail:
            if s[head].isalnum():
                if s[tail].isalnum():
                    if s[head] == s[tail]:
                        head += 1
                    else:
                        return False
                tail -= 1
            else:
                head += 1
        return True

    def isPalindrome3(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

    def isPalindrome4(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.translate(str.maketrans("", "", string.punctuation))
        s = s.lower()
        s = s.replace(" ", "")
        return s == s[::-1]

# str.maketrans(x[, y[, z]]) 静态方法
# 给方法 str.translate() 创建字符映射 dict；只有一个参数时，必须是 Unicode序数（整数）或字符（长度为 1 的 String，会被转换为
# Unicode 序数）映射到 Unicode 序数（整数）、任意长度字符串、None 的 dict 字典；如果有两个参数 xy，则必须是等长字符串，x 中字
# 符映射到 y 中相同位置的字符，映射字典中 key 和 value 是单个字符转换的 Unicode 序数，如果 x 中存在重复字符则取用索引较大的字
# 符来映射；第三个参数 z 必须为字符串，其字符都会映射到 None，z 可以不与 xy 等长，如果 z 与 x 中字符重复则优先映射到 None 而
# 不映射到 y。
