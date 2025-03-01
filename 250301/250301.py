def applyOperations(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    return [x for x in nums if x != 0] + [x for x in nums if x == 0]


nums = [1,2,2,1,1,0]
applyOperations(nums)