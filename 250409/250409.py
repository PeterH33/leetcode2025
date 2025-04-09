def minOperations(nums: list[int], k: int) -> int:
    if any(val < k for val in nums):
        return -1
    snums = set(nums)
    if k in snums:
        return len(snums) - 1
    else:
        return len(snums)
    
nums = [5,2,5,4,5]
k = 2
minOperations(nums, k)