class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        num_list = [1] * n
        num_list[0], num_list[1] = 0, 0

        for i in range(2, int(pow(n, 0.5)) + 1):
            if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
                num_list[i * i::i] = [0] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

        return sum(num_list)


if __name__ == "__main__":
    print(Solution().countPrimes(10))  # 4
    print(Solution().countPrimes(499979))  # 41537
