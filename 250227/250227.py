def lenLongestFibSubseq(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    maxFCount = 0
    sArr = set(arr)

    def getFib(i,j,k):
        seq = [i,j,k]
        while seq[-1] in sArr:
            seq.append(seq[-1]+seq[-2])
        print(seq)
        return len(seq)-1

    for i, v in enumerate(arr):
        # If this happens, we know that all values above i will also be > arr[-1] so the problem is done
        if arr[i] + arr[i+1] > arr[-1]:
            print('break size')
            return maxFCount
        
        for j, w in enumerate(arr[i+1:]):
            if arr[i] + arr[j+i+1] in sArr:
                # A sequence head was found, get the length of it
                maxFCount = max(maxFCount, getFib(arr[i], arr[j+i+1], arr[i]+arr[j+i+1]))
                if maxFCount >= len(arr) - i:
                    return maxFCount
    return maxFCount

arr = [1,2,3,4,5,6,7,8]
arr = [2,4,7,8,9,10,14,15,18,23,32,50]
lenLongestFibSubseq(arr)
