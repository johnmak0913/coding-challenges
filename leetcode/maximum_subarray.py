
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        largestSum = [0] * n
        largestSum[0] = nums[0]
        
        for i in range(1, n):
            largestSum[i] = max(nums[i], largestSum[i - 1] + nums[i])
        
        return max(largestSum)
        
