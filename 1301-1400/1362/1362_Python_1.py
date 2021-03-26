from typing import List


def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield [k, n // k]
        k += 1
    if k * k == n:
        yield [k, k]


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res1 = min(factors(num + 1), key=lambda x: abs(x[1] - x[0]))
        res2 = min(factors(num + 2), key=lambda x: abs(x[1] - x[0]))
        return min(res1, res2, key=lambda x: abs(x[1] - x[0]))


if __name__ == "__main__":
    print(Solution().closestDivisors(8))  # [3,3]
    print(Solution().closestDivisors(123))  # [5,25]
    print(Solution().closestDivisors(999))  # [40,25]
