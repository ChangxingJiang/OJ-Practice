from typing import List


def factors(n):
    res = []
    k = 1
    while k * k < n:
        if n % k == 0:
            res.append(k)
            res.append(n // k)
        k += 1
    if k * k == n:
        res.append(k)
    return res


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            f = factors(num)
            if len(f) == 4:
                ans += sum(f)
        return ans


if __name__ == "__main__":
    print(Solution().sumFourDivisors(nums=[21, 4, 7]))  # 32
