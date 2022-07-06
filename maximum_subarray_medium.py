class Solution(object):
    def maxSubArray(self, nums):
        maxSofar = nums[0]
        currentSum = nums[0]
        
        for i in range(1,len(nums)):
            if currentSum < 0:
                currentSum = 0
            currentSum += nums[i]
            if currentSum > maxSofar:
                maxSofar = currentSum
        return maxSofar
