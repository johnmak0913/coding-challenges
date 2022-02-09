
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        
        nums.sort()
        
        for pointer1 in range(n - 2):
            pointer2 = pointer1 + 1
            pointer3 = n - 1
            
            if pointer1 > 0 and nums[pointer1] == nums[pointer1 - 1]:
                continue
            
            while pointer2 < pointer3:
                sum = nums[pointer1] + nums[pointer2] + nums[pointer3]
                
                if sum < 0:
                    pointer2 += 1
                elif sum > 0:
                    pointer3 -= 1
                elif pointer2 > pointer1 + 1 and nums[pointer2] == nums[pointer2 - 1]:
                    pointer2 += 1
                elif pointer3 < n - 1 and nums[pointer3] == nums[pointer3 + 1]:
                    pointer3 -= 1
                else:
                    ans.append([nums[pointer1], nums[pointer2], nums[pointer3]])
                    pointer3 -= 1
        
        return ans
			
