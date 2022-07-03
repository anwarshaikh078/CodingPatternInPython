class Solution(object):
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        f = 0
        s = len(numbers)-1
        while(f < s):
            currentSum = numbers[f] + numbers[s]
            
            if currentSum < target:
                f += 1
            elif currentSum > target:
                s -= 1
            else:
                a.append(f+1)
                a.append(s+1)
                break
                
        return a 
