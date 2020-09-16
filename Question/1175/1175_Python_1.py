class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrimes(k: int) -> int:
            if k < 2:
                return 0

            num_list = [True] * k
            num_list[0], num_list[1] = False, False

            for i in range(2, int(pow(k, 0.5)) + 1):
                if num_list[i]:
                    num_list[i * i::i] = [False] * ((k - i * i - 1) // i + 1)

            return sum(num_list)

        prime_num = countPrimes(n + 1)
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
