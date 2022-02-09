
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maxPosition = [0] * n
        maxPosition[0] = nums[0]
        
        for i in range(1, n):
            if maxPosition[i - 1] < i:
                return False
            
            maxPosition[i] = max(maxPosition[i - 1], i + nums[i])
        
        return maxPosition[n - 1] >= n - 1
			
