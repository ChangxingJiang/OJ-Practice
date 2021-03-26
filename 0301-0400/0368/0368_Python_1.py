from typing import List


def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        count = {n: i for i, n in enumerate(nums)}
        dp = [1] * len(nums)
        res = [[nums[i]] for i in range(len(nums))]

        ans = 0
        for i in range(len(nums)):
            for factor in factors(nums[i]):
                if factor in count:
                    if factor != nums[i]:
                        if dp[count[factor]] + 1 > dp[i]:
                            dp[i] = dp[count[factor]] + 1
                            res[i] = res[count[factor]] + [nums[i]]
                            if dp[i] > dp[ans]:
                                ans = i

        return res[ans]


if __name__ == "__main__":
    print(Solution().largestDivisibleSubset([1, 2, 3]))  # [1,2]
    print(Solution().largestDivisibleSubset([1, 2, 4, 8]))  # [1,2,4,8]
