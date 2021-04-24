class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b >= c:
            return (a + b + c) // 2
        else:
            return a + b


if __name__ == "__main__":
    print(Solution().maximumScore(2, 4, 6))  # 6
    print(Solution().maximumScore(4, 4, 6))  # 7
    print(Solution().maximumScore(1, 8, 8))  # 8

    # 自制测试用例
    print(Solution().maximumScore(1, 3, 8))  # 4
