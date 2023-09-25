
# Optimized maxProfit function using dynamic programming

def maxProfit(price, start, end):
    # If the stocks can't be bought
    if (end <= start):
        return 0

    # Create a memoization table to store previously calculated profits
    memo = [[-1] * (end + 1) for _ in range(start + 1)]

    def calculateProfit(price, start, end, memo):
        # If the profit for this range has already been calculated, return it
        if memo[start][end] != -1:
            return memo[start][end]

        # Initialise the profit
        profit = 0

        # The day at which the stock must be bought
        for i in range(start, end, 1):

            # The day at which the stock must be sold
            for j in range(i + 1, end + 1):

                # If buying the stock at ith day and selling it at jth day is profitable
                if (price[j] > price[i]):

                    # Update the current profit
                    curr_profit = price[j] - price[i] + calculateProfit(price, start, i - 1, memo) + calculateProfit(price, j + 1, end, memo)

                    # Update the maximum profit so far
                    profit = max(profit, curr_profit)

        # Store the calculated profit in the memoization table
        memo[start][end] = profit

        return profit

    return calculateProfit(price, start, end, memo)


# Optimized longestCommonSubsequence_brute function using dynamic programming

def longestCommonSubsequence_brute(text1, text2):
    if not text1 or not text2:
        return 0

    # Create a memoization table to store previously calculated lengths of common subsequences
    memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    def calculateLCS(text1, text2, memo):
        # If the length of common subsequence for this pair of texts has already been calculated, return it
        if memo[len(text1)][len(text2)] != -1:
            return memo[len(text1)][len(text2)]

        if text1[-1] == text2[-1]:
            # If the last characters of both texts are the same, add 1 to the length of common subsequence
            length = 1 + calculateLCS(text1[:-1], text2[:-1], memo)
        else:
            # If the last characters of both texts are different, calculate the length of common subsequence by considering both possibilities
            length = max(calculateLCS(text1[:-1], text2, memo), calculateLCS(text1, text2[:-1], memo))

        # Store the calculated length of common subsequence in the memoization table
        memo[len(text1)][len(text2)] = length

        return length

    return calculateLCS(text1, text2, memo)
