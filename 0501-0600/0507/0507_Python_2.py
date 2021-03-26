class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        factors = [1]
        for i in range(2, int(pow(num, 0.5) + 1)):
            if num % i == 0:
                factors.append(i)
                factors.append(num / i)
        return sum(factors) == num


if __name__ == "__main__":
    print(Solution().checkPerfectNumber(28))  # True
    print(Solution().checkPerfectNumber(6))  # True
    print(Solution().checkPerfectNumber(496))  # True
    print(Solution().checkPerfectNumber(30402457))  # False
    print(Solution().checkPerfectNumber(1))  # False
    print(Solution().checkPerfectNumber(-6))  # False
