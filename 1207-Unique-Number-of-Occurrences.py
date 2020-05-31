class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        
        Runtime: 16 ms, faster than 98.92%
        Memory Usage: 12.8 MB, less than 100.00%
        """
        counts = {}
        
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
                
        occurences = counts.values()
        uniqueOccurences = set(occurences)
        
        return len(occurences) == len(uniqueOccurences)