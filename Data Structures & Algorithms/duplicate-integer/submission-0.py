class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCounts = {}
        for i in nums:
            numCounts[i] = numCounts.get(i, 0) + 1
            if numCounts[i] > 1:
                return True
        
        return False