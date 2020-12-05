import math


class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == n * n:
            return 1

        choices = []
        for i in range(n + 1):
            for j in range(n + 1):
                if (n - i) * (n - j) == n * n - k:
                    choices.append(tuple(sorted([i, j])))

        # print(choices)

        if not choices:
            return 0

        ans = 0
        for choice in choices:
            n1, n2 = choice
            c1, c2 = n, n1
            d1, d2 = n, n2
            v1 = int(math.factorial(c1) / (math.factorial(c1 - c2) * math.factorial(c2)))
            v2 = int(math.factorial(d1) / (math.factorial(d1 - d2) * math.factorial(d2)))
            ans += v1 * v2
        return ans


if __name__ == "__main__":
    print(Solution().paintingPlan(2, 2))  # 4
    print(Solution().paintingPlan(2, 1))  # 0
    print(Solution().paintingPlan(2, 4))  # 1
    print(Solution().paintingPlan(4, 13))  # 32
