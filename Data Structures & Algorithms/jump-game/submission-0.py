class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            # If we cannot reach this index, we're stuck
            if i > farthest:
                return False

            # Update the farthest reachable position
            farthest = max(farthest, i + nums[i])

            # If we've reached the last index, we're done
            if farthest >= len(nums) - 1:
                return True

        return True
