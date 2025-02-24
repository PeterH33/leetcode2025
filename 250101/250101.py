def maxScore(self, s):
    # Track the max and compare it using count.
    max = 0
    for i in range(1, len(s)):
        if s[:i].count('0') + s[i:].count('1') > max:
            max = s[:i].count('0') + s[i:].count('1')
    return max