class Solution:
    def countPrimes(self, n: int) -> int:
        prime_list = []
        for c in range(2, n):
            for i in prime_list:
                if c % i == 0:
                    break
            else:
                prime_list.append(c)
        return len(prime_list)


if __name__ == "__main__":
    print(Solution().countPrimes(10))  # 4
    print(Solution().countPrimes(499979))  # 41537