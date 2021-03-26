from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)

        ans = 0

        for i in range(size - 2):
            l, r = i + 1, size - 1
            aim = target - nums[i]
            while l < r:
                if nums[l] + nums[r] >= aim:
                    r -= 1
                else:
                    ans += r - l
                    l += 1

        return ans



if __name__ == "__main__":
    print(Solution().threeSumSmaller(nums=[-2, 0, 1, 3], target=2))  # 2
