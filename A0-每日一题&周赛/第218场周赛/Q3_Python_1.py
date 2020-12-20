class Solution:
    _MOD = 1000000007

    def concatenatedBinary(self, n: int) -> int:
        now = 0
        for i in range(1, n + 1):
            now <<= i.bit_length()
            now += i
            now %= self._MOD
        return now


if __name__ == "__main__":
    print(Solution().concatenatedBinary(1))  # 1
    print(Solution().concatenatedBinary(3))  # 27
    print(Solution().concatenatedBinary(12))  # 505379714
