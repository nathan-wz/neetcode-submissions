class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        result = []

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference not in nums_dict:
                nums_dict[nums[i]] = i
                continue
            else:
                result += [nums_dict[difference], i]
                break
            
        return result
                
