from collections import deque

def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    res = []
    nums1 = deque(nums1)
    nums2 = deque(nums2)
    while nums1 and nums2:
        if nums1[0][0] == nums2[0][0]:
            a = nums1.popleft()
            b = nums2.popleft()
            res.append([a[0], a[1]+b[1]])
        elif nums1[0][0] < nums2[0][0]:
            res.append(nums1.popleft())
        else:
            res.append(nums2.popleft())
    if nums1:
        res.extend(nums1)
    elif nums2:
        res.extend(nums2)
    return res