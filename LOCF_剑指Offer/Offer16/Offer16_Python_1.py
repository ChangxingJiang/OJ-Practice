class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        for i in range(n):
            ans *= x
        return ans


if __name__ == "__main__":
    print(Solution().myPow(2, 10))  # 1024
    print(Solution().myPow(2.1, 3))  # 9.261
    print(Solution().myPow(2, -2))  # 0.25
