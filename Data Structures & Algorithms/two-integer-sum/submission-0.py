class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            answer = target - n
            if answer in seen:
                return [seen[answer], i]

            seen[n] = i

        return []