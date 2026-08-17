class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        numCounts = {}

        for i in nums:
            numCounts[i] = numCounts.get(i, 0) + 1
            if numCounts[i] > target:
                return i
        
        return nums[0]