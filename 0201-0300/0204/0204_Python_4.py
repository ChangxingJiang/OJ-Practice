class Solution:
    def countPrimes(self, n: int) -> int:
        num_list = [True for _ in range(n)]

        for i in range(2, n):
            if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
                for j in range(2 * i, n, i):
                    num_list[j] = False

        ans = 0
        for i in range(2, n):
            if num_list[i]:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countPrimes(10))  # 4
    print(Solution().countPrimes(499979))  # 41537
