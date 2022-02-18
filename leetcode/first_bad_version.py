# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def searchBadVersion(start, end):
            if end == 1 or isBadVersion(start): 
                return start
            
            pivot = (start + end) / 2
            if isBadVersion(pivot):
                if pivot != 1 and not isBadVersion(pivot - 1):
                    return pivot
                else:
                    return searchBadVersion(start, pivot)
            else:
                return searchBadVersion(pivot + 1, end)
        
        return searchBadVersion(1, n)
	
