class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif not stones:
            return 0

        heaviest_stones = sorted(stones, reverse=True)
        x = heaviest_stones.pop(0)
        y = heaviest_stones.pop(0)
        
        heaviest_stones.append(abs(x - y))

        stone = self.lastStoneWeight(heaviest_stones)
        return stone