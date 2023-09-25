def coinChange(coins, amount):
    def recursiveChange(remaining):
        # base case: if remaining amount is negative, return -1
        if remaining < 0:
            return -1
        # base case: if remaining amount is 0, return 0 (no more coins needed)
        if remaining == 0:
            return 0
        # initialize minimum to a large value
        minimum = float('inf')
        for coin in coins:
            result = recursiveChange(remaining - coin)
            # if result is not -1 and is smaller than current minimum, update minimum
            if result >= 0 and result < minimum:
                minimum = result + 1
        # if minimum is still inf, return -1, else return minimum
        return -1 if minimum == float('inf') else minimum

    return recursiveChange(amount)

def longestCommonSubsequence(text1, text2):
    def lcs(i, j):
        if i < 0 or j < 0:
            return 0
        if text1[i] == text2[j]:
            return 1 + lcs(i - 1, j - 1)
        else:
            return max(lcs(i - 1, j), lcs(i, j - 1))

    return lcs(len(text1) - 1, len(text2) - 1)