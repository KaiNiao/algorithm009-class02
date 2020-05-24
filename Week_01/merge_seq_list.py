# coding: utf-8

from typing import List


class Solution(object):
    """合并两个有序数组成为一个有序数组"""
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """合并后排序"""
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """双指针法"""
        if 0 == m:  # 直接原地拷贝nums2，nums1 = nums2语句会修改了nums1的指向
            nums1[:n] = nums2[:n]
        elif 0 == n:  # 直接返回
            pass
        else:
            i = m - 1
            j = n - 1
            p = m + n - 1  # 当前位置
            
            while i >= 0 and j >= 0:
                if nums1[i] <= nums2[j]:  # nums1 的元素尽量少动
                    nums1[p] = nums2[j]
                    j -= 1
                    p -= 1
                else:
                    nums1[p] = nums1[i]
                    i -= 1
                    p -= 1                
            
            if j >= 0:  # 第二个数组的表头有剩余元素
                nums1[p - j: j + 1] = nums2[: j + 1]  # 必然有 p - j == 0，因为剩下的是最小的，必然是copy到最前面 
    
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge_1(nums1, m, nums2, n)
print(nums1)
