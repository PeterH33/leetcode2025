def numOfSubarrays(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    mod = 1000000007
    prefixSum = 0
    oddCount = 0

    for val in arr:
        prefixSum += val
        oddCount += prefixSum % 2
    oddCount += (len(arr) - oddCount) * oddCount
    return oddCount % mod

arr=[1,3,5]
arr=[100,100,99,99]
arr = [1,2,3,4,5,6,7]
numOfSubarrays(arr)
