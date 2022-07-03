class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(0,len(nums)):
            a = a ^ nums[i]
        return a
        
