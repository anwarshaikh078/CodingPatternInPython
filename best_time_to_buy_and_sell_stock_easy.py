class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        minSofar = prices[0]
        
        for i in range(1,len(prices)):
            profit = prices[i] - minSofar
            if (ans < profit):
                ans = profit
            
            if minSofar > prices[i]:
                minSofar = prices[i]
        
        return ans
