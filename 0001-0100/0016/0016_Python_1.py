from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans_num, ans_val = float("inf"), float("inf")

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 如果和上一个数相同则跳过
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                v = nums[i] + nums[j] + nums[k]
                if v == target:
                    return target
                if abs(v - target) < ans_val:
                    ans_num, ans_val = v, abs(v - target)

                if v > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return ans_num


if __name__ == "__main__":
    print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))  # 2
    print(Solution().threeSumClosest(nums=[0, 1, 2], target=3))  # 3
    print(Solution().threeSumClosest(nums=[1, 1, 1, 0], target=-100))  # 2
