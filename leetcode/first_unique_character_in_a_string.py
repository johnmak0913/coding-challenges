
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
				
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = 1
            else:
                charMap[s[i]] += 1
        
        for i in range(len(s)):
            if charMap[s[i]] == 1:
                return i
       	
        return -1
			
