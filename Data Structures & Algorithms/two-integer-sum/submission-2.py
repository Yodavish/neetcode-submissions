class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            answer = target - num
            if answer in seen:
                return [seen[answer], i]
            
            seen[num] = i
