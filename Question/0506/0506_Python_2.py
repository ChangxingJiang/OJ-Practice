from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        order = [-1] * (max(nums) + 1)
        for i in range(len(nums)):
            order[nums[i]] = i
        rank = 1
        for i in order[::-1]:
            if i != -1:
                if rank == 1:
                    nums[i] = "Gold Medal"
                elif rank == 2:
                    nums[i] = "Silver Medal"
                elif rank == 3:
                    nums[i] = "Bronze Medal"
                else:
                    nums[i] = str(rank)
                rank += 1
        return nums


if __name__ == "__main__":
    print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))  # ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
