class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for i in range(L, R + 1):
            if bin(i).count("1") in primes:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countPrimeSetBits(6, 10))  # 4
    print(Solution().countPrimeSetBits(10, 15))  # 5
