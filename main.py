
# Optimized maxProfit function using dynamic programming

def maxProfit(price, start, end):
    # If the stocks can't be bought
    if (end <= start):
        return 0
    
    # Create a memoization table to store previously calculated profits
    memo = [[-1] * (end+1) for _ in range(start+1)]
    
    # Helper function to calculate the maximum profit
    def calculateProfit(start, end):
        # If the profit has already been calculated, return it from the memoization table
        if memo[start][end] != -1:
            return memo[start][end]
        
        # Initialise the profit
        profit = 0
        
        # The day at which the stock must be bought
        for i in range(start, end, 1):
            # The day at which the stock must be sold
            for j in range(i+1, end+1):
                # If buying the stock at ith day and selling it at jth day is profitable
                if (price[j] > price[i]):
                    # Update the current profit
                    curr_profit = price[j] - price[i] + calculateProfit(start, i - 1) + calculateProfit(j + 1, end)
                    # Update the maximum profit so far
                    profit = max(profit, curr_profit)
        
        # Store the calculated profit in the memoization table
        memo[start][end] = profit
        
        return profit
    
    return calculateProfit(start, end)


# Optimized longestCommonSubsequence_brute function using dynamic programming

def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0
    
    # Create a memoization table to store previously calculated lengths of common subsequences
    memo = [[-1] * (len(text2)+1) for _ in range(len(text1)+1)]
    
    # Helper function to calculate the length of the longest common subsequence
    def calculateLCS(text1, text2, m, n):
        # If the length of common subsequence has already been calculated, return it from the memoization table
        if memo[m][n] != -1:
            return memo[m][n]
        
        # If the last characters of both texts are the same
        if text1[m-1] == text2[n-1]:
            # Calculate the length of the longest common subsequence by excluding the last characters
            memo[m][n] = 1 + calculateLCS(text1, text2, m-1, n-1)
        else:
            # Calculate the length of the longest common subsequence by excluding the last character of text1
            lcs1 = calculateLCS(text1, text2, m-1, n)
            # Calculate the length of the longest common subsequence by excluding the last character of text2
            lcs2 = calculateLCS(text1, text2, m, n-1)
            # Choose the maximum length of the two calculated subsequences
            memo[m][n] = max(lcs1, lcs2)
        
        return memo[m][n]
    
    return calculateLCS(text1, text2, len(text1), len(text2))
