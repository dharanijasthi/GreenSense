def climbStairs_brute(n):
    if n <= 1:
        return 1
    return climbStairs_brute(n - 1) + climbStairs_brute(n - 2)



def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0
    if text1[-1] == text2[-1]:
        return 1 + longestCommonSubsequence_brute(text1[:-1], text2[:-1])
    else:
        return max(longestCommonSubsequence_brute(text1[:-1], text2), longestCommonSubsequence_brute(text1, text2[:-1]))