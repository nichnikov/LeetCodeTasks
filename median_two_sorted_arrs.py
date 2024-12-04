"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

import numpy as np


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums = np.concatenate((nums1, nums2), axis=0)
    return np.median(np.sort(nums))

if __name__ == "__main__":

    nums1, nums2 = np.array([1, 3]), np.array([2])
    print(findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [1,2], [3,4]
    print(findMedianSortedArrays(nums1, nums2))
