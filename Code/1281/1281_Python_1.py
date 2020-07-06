class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n:
            digit = n % 10
            n = n // 10
            product *= digit
            total += digit
        return product - total


if __name__ == "__main__":
    print(Solution().subtractProductAndSum(234))  # 15
    print(Solution().subtractProductAndSum(4421))  # 21
