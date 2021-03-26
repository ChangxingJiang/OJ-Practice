class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        def count(xx, nn):
            if nn == 0:
                return 1
            if nn == 1:
                return x
            a = nn // 2
            b = nn - a
            if a == b:
                val = count(xx, a)
                return val * val
            else:
                return count(xx, a) * count(xx, b)

        return count(x, n)



if __name__ == "__main__":
    print(Solution().myPow(2, 10))  # 1024
    print(Solution().myPow(2.1, 3))  # 9.261
    print(Solution().myPow(2, -2))  # 0.25
