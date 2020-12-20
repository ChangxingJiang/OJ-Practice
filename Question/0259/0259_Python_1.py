from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        size = len(nums)

        ans = 0

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if nums[i] + nums[j] + nums[k] < target:
                        ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().threeSumSmaller(nums=[-2, 0, 1, 3], target=2))  # 2
