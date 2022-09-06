class Solution(object):
    def maxProfitBruteForce(self, prices):          #time complexity O(n^2). Loop runs n(n-1)/2 times. Space complexity O(1) two variables used (maxprofit, profit)
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit



    def maxProfitOnePass(self, prices):         #time complexity O(n) from single pass, space complexity O(1) two variables used
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit

print(Solution().maxProfitOnePass([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfitBruteForce([7, 1, 5, 3, 6, 4]))


