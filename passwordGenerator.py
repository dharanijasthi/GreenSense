
# Optimized maxProfit function using dynamic programming

def maxProfit(price, start, end):
    # If the stocks can't be bought
    if (end <= start):
        return 0
    
    # Create a table to store the maximum profit for each day
    profit_table = [0] * (end + 1)
    
    # Iterate through the price list from the end to the start
    for i in range(end, start - 1, -1):
        # Initialize the maximum profit for the current day
        max_profit = 0
        
        # Iterate through the price list from the current day to the end
        for j in range(i + 1, end + 1):
            # If buying the stock at ith day and selling it at jth day is profitable
            if (price[j] > price[i]):
                # Calculate the profit for the current transaction
                curr_profit = price[j] - price[i] + profit_table[j + 1]
                
                # Update the maximum profit for the current day
                max_profit = max(max_profit, curr_profit)
        
        # Update the maximum profit for the current day in the profit table
        profit_table[i] = max_profit
    
    # Return the maximum profit for the first day
    return profit_table[start]


# Optimized longestCommonSubsequence_brute function using dynamic programming

def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0
    
    # Create a table to store the length of the longest common subsequence
    lcs_table = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    
    # Iterate through the characters of text1 and text2
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            # If the characters are equal, increment the length of the longest common subsequence
            if text1[i - 1] == text2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            # If the characters are not equal, take the maximum length from the previous rows or columns
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
    
    # Return the length of the longest common subsequence
    return lcs_table[-1][-1]
