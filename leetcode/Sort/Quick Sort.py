# !/usr/bin/env python3
# -*- coding:utf-8 -*-  
# @author: Shengjia Yan
# @date: 2019-10-27 Sunday
# @email: i@yanshengjia.com
# Copyright @ Shengjia Yan. All Rights Reserved.


def lomuto_partition(nums, lo, hi):
    pivot = nums[hi]    # last element as pivot
    i = lo
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1  # left side of i are smaller than pivot
    nums[i], nums[hi] = nums[hi], nums[i]
    return i


def quick_sort(nums, lo, hi):
    if lo < hi:
        pivot = lomuto_partition(nums, lo, hi)
        quick_sort(nums, lo, pivot - 1)
        quick_sort(nums, pivot + 1, hi)
    return nums


if __name__ == "__main__":
    nums = [1, 3, 6, 7, 2, 4, 5, 8]
    print(quick_sort(nums, 0, len(nums)-1))
