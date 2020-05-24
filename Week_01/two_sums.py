# coding: utf-8

from typing import List


class Solution(object):
    def two_sums(self, nums: List[int], target: int) -> List[int]:
        """"暴力解法"""
        for i in range(len(nums) - 1):
            # for j in range(len(nums)):  有重复，已计算过
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_sums_1(self, nums: List[int], target: int) -> List[int]:
        """两遍哈希表"""
        hashmap = {}
        for i, value in enumerate(nums):
            hashmap[value] = i
        
        for i, value in enumerate(nums):
            temp = target - value
            j = hashmap.get(temp)
            if j is not None and i != j:
                return [i, j]

    def two_sums_2(self, nums: List[int], target: int) -> List[int]:
        """一遍哈希表"""
        hashmap = {}
        for i, value in enumerate(nums):
            temp = target - value
            if temp in hashmap:  # 循环
                j = hashmap.get(temp)
                if i != j:
                    return [j, i]
            hashmap[value] = i


s = Solution()
nums = [2, 7, 11, 15]
target = 9
indexs = s.two_sums_2(nums, target)
print(indexs)
