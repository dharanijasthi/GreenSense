def maxProfit(price, start, end):
  
    # If the stocks can't be bought
    if (end <= start):
        return 0
  
    # Initialise the profit
    profit = 0
  
    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):
  
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
  
            # If buying the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
  
                # Update the current profit
                curr_profit = price[j] - price[i] +\
                    maxProfit(price, start, i - 1) + \
                    maxProfit(price, j + 1, end)
  
                # Update the maximum profit so far
                profit = max(profit, curr_profit)
  
    return profit


def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0
    if text1[-1] == text2[-1]:
        return 1 + longestCommonSubsequence_brute(text1[:-1], text2[:-1])
    else:
        return max(longestCommonSubsequence_brute(text1[:-1], text2), longestCommonSubsequence_brute(text1, text2[:-1]))