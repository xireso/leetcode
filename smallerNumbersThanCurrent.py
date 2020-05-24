class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

        :type nums: List[int]
        :rtype: List[int]
        
        Runtime: 52 ms, faster than 73.68% 
        Memory Usage: 12.7 MB, less than 100.00% 
        
        Overall, O(n+m) runtime, O(1) space
        """
        
        MAX_VALUE = 101
        # create buckets, one for each number
        # to hold how many times a number appears
        counts = [0]*MAX_VALUE      # hallo
                                   
        # O(n), populates counts list with occurance # of each number
        for num in nums:      
            counts[num] += 1
                    
        # create a cumulative list to hold how many numbers appear before this number
        cumulative = [counts[0]] + [0]* (MAX_VALUE-1)
        
        # populate cumulative list
        for i in range(1, len(counts) - 1):     # O(m)
            cumulative[i] = cumulative[i-1] + counts[i]
        
        answer = []
        
        # index into cumulative to find how many numbers appear before this number
        # and add to answer
        for num in nums:
            nums_smaller = cumulative[num-1]
            answer.append(nums_smaller)
        
        return answer