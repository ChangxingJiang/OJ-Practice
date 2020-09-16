class Solution:
    def countPrimes(self, n: int) -> int:
        def is_primes(c):
            """
            判断c是否为质数
            """
            for i in range(2, int(pow(c, 0.5)) + 1):
                if c % i == 0:
                    return False
            return True

        ans = 0
        for j in range(2, n):
            if is_primes(j):
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countPrimes(10))  # 4
