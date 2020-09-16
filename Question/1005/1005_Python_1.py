from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        number = []
        minus = []
        for a in A:
            if a >= 0:
                number.append(a)
            else:
                minus.append(a)
        minimum = min(number)
        minus.sort(reverse=True)

        out = 1
        for _ in range(K):
            if len(minus) > 0:
                n = -minus.pop(-1)
                if n < minimum:
                    minimum = n
                number.append(n)
            else:
                out *= -1
        return sum(number) + sum(minus) - minimum + out * minimum


if __name__ == "__main__":
    print(Solution().largestSumAfterKNegations(A=[4, 2, 3], K=1))  # 5
    print(Solution().largestSumAfterKNegations(A=[3, -1, 0, 2], K=3))  # 6
    print(Solution().largestSumAfterKNegations(A=[2, -3, -1, 5, -4], K=2))  # 13
