class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n+1):
            bits.append(len(bin(i)[2:].replace("0","")))
    
        return bits
        