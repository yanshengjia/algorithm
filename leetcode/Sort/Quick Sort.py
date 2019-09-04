def quicksort(l, start, end):
    if start > end:
        return
    left = start
    right = end
    pivot = l[left]
    while left < right:
        # 让右边游标往左移动，目的是找到小于 pivot 的值，放到 left 游标位置
        while left < right and l[right] >= pivot:
            right -= 1
        l[left] = l[right]
        # 让左边游标往右移动，目的是找到大于 pivot 的值，放到 right 游标位置
        while left < right and l[left] < pivot:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    quicksort(l, start, left-1)
    quicksort(l, left, end)