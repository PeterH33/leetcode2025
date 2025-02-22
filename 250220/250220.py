class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        # First we sort the nums array, because the length of all strings are the same, this sorting will be numerical.
        n = len(nums)
        nums.sort()

        # Now we simply start counting
        for i in range(n):
            if nums[i] != f'{(bin(i)[2:]):>0{n}s}':
                return bin(i)[2:].zfill(n)
        return bin(n)[2:].zfill(n)
    
        # As soon as the binary string from nums is not the same as a binary projection of i, we return the answer.
        # There are two different versions of getting a binary representation of i, this is one of the few realms where other languages are a bit more straight forward, Python gives binary in strings of format 0bXXXXXX so we must strip off the 0b for comparison, or add it to nums[i]
        # zfill front loads 0s up to the required size string, so does :>0{n}s
