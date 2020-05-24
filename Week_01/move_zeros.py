# coding: utf-8
# https://leetcode-cn.com/problems/move-zeroes/
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

from typing import List


class Solution(object):
    def move_zeros_1(self, nums: List[int]) -> None:
        """双指针法，一维数组的坐标变换，所有非零元素移动到数组的末尾"""
        cur = 0  # 记录当前非零元素的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur] = nums[i]
                cur += 1
        
        for i in range(cur, len(nums)):
            nums[i] = 0

    def move_zeros_2(self, nums: List[int]) -> None:
        """暴力解法，所有零元素移动到数组的末尾"""
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            else:  # 遇到零元素则与下一个非零元素交换
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

    def move_zeros_3(self, nums: List[int]) -> List[int]:
        """暴力解法"""
        i = 0  # i指向非零索引位置
        filter_list = [None] * len(nums)
        for j in range(len(nums)):
            if nums[j] != 0:
                filter_list[i] = nums[j]
                i += 1
            else:
                filter_list[j] = 0
        
        return filter_list


s = Solution()
# nums = [0, 1, 5, 0, 2]
nums = [2, 0, 5, 0, 3]
# s.move_zeros_1(nums)
# print(nums)

print(s.move_zeros_3(nums))
