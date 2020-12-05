from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        now = nums[0]
        last = nums[0]

        ans = []

        for i in range(1, len(nums)):
            if nums[i] != last + 1:
                ans.append(str(now) + "->" + str(last) if now != last else str(now))
                now = last = nums[i]
            else:
                last += 1

        ans.append(str(now) + "->" + str(last) if now != last else str(now))

        return ans


if __name__ == "__main__":
    # ["0->2","4->5","7"]
    print(Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]))

    # ["0","2->4","6","8->9"]
    print(Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))

    # []
    print(Solution().summaryRanges(nums=[]))

    # ["-1"]
    print(Solution().summaryRanges(nums=[-1]))

    # ["0"]
    print(Solution().summaryRanges(nums=[0]))
