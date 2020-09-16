class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1  # 将res左移一位
            res += n & 1  # 使用或运算，判断n的最右一位是否为1，如果为1则填到res的最右一位中
            n >>= 1  # 将n右移一位
        return res


if __name__ == "__main__":
    print(Solution().reverseBits(int("0b00000010100101000001111010011100", 2)))  # 00111001011110000010100101000000
    print(Solution().reverseBits(int("0b11111111111111111111111111111101", 2)))  # 10111111111111111111111111111111
