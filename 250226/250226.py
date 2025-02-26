def maxAbsoluteSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currentMax, currentMin, maxSum, minSum = 0,0,0,0

    for num in nums:
        currentMax = max(currentMax + num, num)
        currentMin = min(currentMin + num, num)
        maxSum = max(maxSum, currentMax)
        minSum = min(minSum, currentMin)

    return max(abs(maxSum), abs(minSum))

nums = [1,-3,2,3,-4]
nums = [2,-5,1,-4,3,-2]
maxAbsoluteSum(nums)