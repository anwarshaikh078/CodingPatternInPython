class Solution(object):
    def maxSubArray( nums):
        CurrSoFar = 0
        maxSoFar = nums[0]

        for n in nums:
            if CurrSoFar < 0:
                CurrSoFar = 0
            CurrSoFar += n
            maxSoFar = max(maxSoFar, CurrSoFar)

        return maxSoFar

if __name__ == "__main__":
    print(Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))