class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        maxprofit = 0
        retval = 0

        for i in range(len(prices)):
            minimum = min(prices[:i+1])
            if maxprofit < prices[i] - minimum:
                maxprofit = prices[i] - minimum

        retval = maxprofit
        return retval


        