def canPartition(nums: list[int]) -> bool:
    nums.sort()
    n = len(nums)
    for i in range(n):
        if sum(nums[i:]) == sum(nums[:i]):
            return True
    return False

nums = [1,5,11,5]
nums = [1,2,3,5]
canPartition(nums)