class Solution:
    def reverseBits(self, n: int) -> int:
        return int("0b" + "{:032b}".format(n)[::-1], 2)


if __name__ == "__main__":
    print(Solution().reverseBits(int("0b00000010100101000001111010011100", 2)))  # 00111001011110000010100101000000
    print(Solution().reverseBits(int("0b11111111111111111111111111111101", 2)))  # 10111111111111111111111111111111
