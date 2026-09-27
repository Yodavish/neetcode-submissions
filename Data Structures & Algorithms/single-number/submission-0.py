class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = dic.get(n, 0) + 1

        key = next((k for k, v in dic.items() if v == 1), None)
        return key