class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for index, jump_length in enumerate(nums):
            if index > farthest:
                return False
            farthest = max(farthest, index + jump_length)
            if farthest >= len(nums) - 1:
                return True
        return True