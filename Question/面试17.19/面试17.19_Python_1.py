from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        size = len(nums) + 2
        expect = (1 + size) * size // 2
        total = sum(nums)

        disappear = expect - total

        mark = disappear // 2

        expect1 = (1 + mark) * mark // 2
        expect2 = expect - expect1
        total1, total2 = 0, 0

        for n in nums:
            if n <= mark:
                total1 += n
            else:
                total2 += n

        n1 = expect1 - total1
        n2 = expect2 - total2

        return [n1, n2]


if __name__ == "__main__":
    print(Solution().missingTwo([1]))  # [2,3]
    print(Solution().missingTwo([2, 3]))  # [1,4]
