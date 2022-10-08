class Solution(object):
    def maxProfit(prices):

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r

            r += 1
        return maxProfit

if __name__ == "__main__":
    print(Solution.maxProfit([7,1,5,3,6,4]))