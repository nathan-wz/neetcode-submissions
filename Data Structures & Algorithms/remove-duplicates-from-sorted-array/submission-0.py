class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        k = 1

        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                nums.pop(r)

            l, r = r, r + 1
            k += 1

        return k