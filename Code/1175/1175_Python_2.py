import bisect


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        prime_num = bisect.bisect_right(primes, n)
        other_num = n - prime_num
        ans = 1
        for i in range(1, prime_num + 1):
            ans *= i
            ans = ans % (10 ** 9 + 7)
        for i in range(1, other_num + 1):
            ans *= i
            ans = ans % (10 ** 9 + 7)
        return ans


if __name__ == "__main__":
    print(Solution().numPrimeArrangements(2))  # 1
    print(Solution().numPrimeArrangements(5))  # 12
    print(Solution().numPrimeArrangements(100))  # 682289015
