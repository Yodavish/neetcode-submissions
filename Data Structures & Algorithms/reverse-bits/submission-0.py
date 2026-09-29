class Solution:
    def reverseBits(self, n: int) -> int:
        bit_num = bin(n)[2:]
        target = 32 - len(bit_num)
        bit_num = ("0" * target) + bit_num
        reverse = bit_num[::-1]
        return int("".join(reverse), 2)