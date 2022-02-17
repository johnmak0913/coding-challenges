
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        current = 0
        next = 1
        
        while next < n:
            if nums[current] == nums[next]:
                next += 1
            else:
                current += 1
                nums[current] = nums[next]
                
        
        return current + 1
			
