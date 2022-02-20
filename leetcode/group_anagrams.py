
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        appearedStrs = {}
        output = []
        
        for i in range(n):
            sortedStr = ''.join(sorted(strs[i]))
            
            if sortedStr in appearedStrs:
                appearedStrs[sortedStr].append(strs[i])
            else:
                appearedStrs[sortedStr] = [strs[i]]
                
        for key in appearedStrs:
            output.append(appearedStrs[key])
            
        return output
	
