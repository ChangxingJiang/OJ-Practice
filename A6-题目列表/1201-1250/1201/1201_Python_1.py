class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().nthUglyNumber(n=3, a=2, b=3, c=5))  # 4
    print(Solution().nthUglyNumber(n=4, a=2, b=3, c=4))  # 6
    print(Solution().nthUglyNumber(n=5, a=2, b=11, c=13))  # 10
    print(Solution().nthUglyNumber(n=1000000000, a=2, b=217983653, c=336916467))  # 1999999984
