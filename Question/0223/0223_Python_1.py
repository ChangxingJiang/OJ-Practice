class Solution:
    @staticmethod
    def count(a, b, c, d):
        if a <= c <= b <= d:
            return b - c
        elif c <= a <= d <= b:
            return d - a
        elif a <= c <= d <= b:
            return d - c
        elif c <= a <= b <= d:
            return b - a
        else:
            return 0

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        res1 = self.count(A, C, E, G)
        res2 = self.count(B, D, F, H)

        s1 = abs(A - C) * abs(B - D)
        s2 = abs(E - G) * abs(F - H)

        return s1 + s2 - res1 * res2


if __name__ == "__main__":
    # 45
    print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))

    # 0
    print(Solution().computeArea(-2, -2, 2, 2, 3, 3, 4, 4))
