
# Optimized coinChange function using dynamic programming
def coinChange(coins, amount):
    # Create a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    # Base case: 0 coins needed for amount 0
    dp[0] = 0
    # Iterate through each amount from 1 to the target amount
    for i in range(1, amount + 1):
        # Iterate through each coin
        for coin in coins:
            # If the coin value is less than or equal to the current amount
            if coin <= i:
                # Update the minimum number of coins needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # If the minimum number of coins needed for the target amount is still infinity, return -1
    if dp[amount] == float('inf'):
        return -1
    # Otherwise, return the minimum number of coins needed
    return dp[amount]

# Optimized longestCommonSubsequence function using dynamic programming
def longestCommonSubsequence(text1, text2):
    # Create a 2D matrix to store the lengths of the longest common subsequences
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    # Iterate through each character in text1
    for i in range(1, len(text1) + 1):
        # Iterate through each character in text2
        for j in range(1, len(text2) + 1):
            # If the characters are equal, add 1 to the length of the longest common subsequence
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # Otherwise, take the maximum length from the previous row or column
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Return the length of the longest common subsequence
    return dp[len(text1)][len(text2)]
