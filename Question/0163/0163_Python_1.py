from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []

        nums.append(upper + 1)
        now = lower - 1
        for n in nums:
            if n - now == 2:
                ans.append(str(n - 1))
            elif n - now > 2:
                ans.append(str(now + 1) + "->" + str(n - 1))
            now = n

        return ans


if __name__ == "__main__":
    # ["2", "4->49", "51->74", "76->99"]
    print(Solution().findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
