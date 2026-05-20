class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = [] 
        for i in range(len(nums)):           
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return_list += [i, j] 
                    return return_list
        