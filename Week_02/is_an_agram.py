# 验证变位词
# 输入为两个字符串，分别为s, t 判断两个字符串是否属于变位字符串
# 举例1
# Input: s = "anagram", t = "nagaram"
# Output: true
# 举例2 
# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def check_string(self, s: str, t: str) -> bool:
        """使用哈希表存储每个元素出现的次数，时间复杂度为O(N)"""
        if len(s) != len(t):
            return False

        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1

        for c in t:
            if hashmap.get(c, 0) <= 0:  # t与s相比，存在过多或过少的元素
                return False
            else:
                hashmap[c] -= 1
        return True

    def check_string_1(self, s: str, t: str) -> bool:
        """直接排序进行比较，时间复杂度为O(NlogN)"""
        return sorted(s) == sorted(t)


aa = Solution()
s = "anagram"
t = "nagaram"
print(aa.check_string(s, t))
