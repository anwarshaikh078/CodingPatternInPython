class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            ans.append(self.getSetBits(i))
        return ans
    
    def getSetBits(self,n):
        count = 0
        for i in range(32):
            if ((n & (1 << i) > 0)):
                count += 1
        return count
