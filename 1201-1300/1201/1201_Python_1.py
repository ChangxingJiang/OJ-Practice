import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left, right = 0, 2 * 10 ** 9

        v1 = (a * b) // math.gcd(a, b)
        v2 = (b * c) // math.gcd(b, c)
        v3 = (a * c) // math.gcd(a, c)
        v4 = (v1 * c) // math.gcd(v1, c)

        while left < right:
            mid = (left + right) // 2

            n1 = mid // a
            n2 = mid // b
            n3 = mid // c
            n4 = mid // v1
            n5 = mid // v2
            n6 = mid // v3
            n7 = mid // v4
            num = n1 + n2 + n3 - n4 - n5 - n6 + n7

            if num < n:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    print(Solution().nthUglyNumber(n=3, a=2, b=3, c=5))  # 4
    print(Solution().nthUglyNumber(n=4, a=2, b=3, c=4))  # 6
    print(Solution().nthUglyNumber(n=5, a=2, b=11, c=13))  # 10
    print(Solution().nthUglyNumber(n=1000000000, a=2, b=217983653, c=336916467))  # 1999999984
    print(Solution().nthUglyNumber(n=10, a=7, b=6, c=8))  # 28
    print(Solution().nthUglyNumber(n=5, a=2, b=3, c=3))  # 8
    print(Solution().nthUglyNumber(n=7, a=7, b=7, c=7))  # 49
