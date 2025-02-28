
def shortestCommonSupersequence(str1: str, str2: str) -> str:
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    def longCS(str1, str2):
        n1, n2 = len(str1), len(str2)
        dp = [['' for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)
        # print(dp)
        return dp[-1][-1]
    
    # print(longCS(str1, str2))

    result, i, j = '', 0, 0
    common = longCS(str1, str2)
    # print(common)
    for c in common:
        # print(f'c:{c}')
        while str1[i] != c:
            # print(f'str1 Loop: {str1[i]} i: {i}')
            result += str1[i]
            i += 1
        while str2[j] != c:
            # print(f'str2 Loop: {str1[i]} i: {i}')
            result += str2[j]
            j+=1
        # print(f'result: {result} + c: {c}')
        result += c
        i+=1
        j+=1
    return result +str1[i:] + str2[j:]



str1='abac'
str2='cab'
str1="bbbaaaba"
str2="bbababbb"
shortestCommonSupersequence(str1, str2)