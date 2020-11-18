class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 0 or B == 0:
            return 0
        elif A >= B:
            return self.multiply(A, B - 1) + A
        else:
            return self.multiply(A - 1, B) + B


if __name__ == "__main__":
    print(Solution().multiply(1, 10))  # 10
    print(Solution().multiply(3, 4))  # 12
