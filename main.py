
def maxProfit(price, start, end):
    if (end <= start):
        return 0

    profit = 0
    min_price = price[start]

    for i in range(start+1, end+1):
        if price[i] < min_price:
            min_price = price[i]
        else:
            curr_profit = price[i] - min_price
            profit = max(profit, curr_profit)

    return profit


def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0

    m = len(text1)
    n = len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
