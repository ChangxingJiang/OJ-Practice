from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 如果和上一个数相同则跳过
                continue
            if nums[i] > 0:  # 如果第1个数已经大于0，则跳过当前选择
                break
            k = len(nums) - 1
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 如果和上一个数相同则跳过
                    continue
                if nums[i] + nums[j] > 0:  # 如果第1个数和第2个数之和已经大于0，则跳过当前选择
                    break
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans


if __name__ == "__main__":
    # [
    #   [-1, 0, 1],
    #   [-1, -1, 2]
    # ]
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

    # []
    print(Solution().threeSum([]))

    # []
    print(Solution().threeSum([0]))

    # [0,0,0]
    print(Solution().threeSum([0, 0, 0, 0]))
