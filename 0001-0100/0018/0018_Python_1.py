from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 处理特殊情况
        if not nums or len(nums) < 4:
            return []

        ans = []
        N = len(nums)
        nums.sort()

        for i1 in range(N - 3):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            if nums[i1] + nums[i1 + 1] + nums[i1 + 2] + nums[i1 + 3] > target:
                break
            if nums[i1] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for i2 in range(i1 + 1, N - 2):
                if i2 > i1 + 1 and nums[i2] == nums[i2 - 1]:
                    continue
                if nums[i1] + nums[i2] + nums[i2 + 1] + nums[i2 + 2] > target:
                    break
                if nums[i1] + nums[i2] + nums[-2] + nums[-1] < target:
                    continue
                i3, i4 = i2 + 1, N - 1
                while i3 < i4:
                    val = nums[i1] + nums[i2] + nums[i3] + nums[i4]
                    if val == target:
                        # print(i1, i2, i3, i4, "->", nums[i1], nums[i2], nums[i3], nums[i4])
                        ans.append([nums[i1], nums[i2], nums[i3], nums[i4]])
                        while i3 < i4 and nums[i3] == nums[i3 + 1]:
                            i3 += 1
                        i3 += 1
                        while i3 < i4 and nums[i4] == nums[i4 - 1]:
                            i4 -= 1
                        i4 -= 1
                    elif val < target:
                        i3 += 1
                    else:
                        i4 -= 1

        return ans


if __name__ == "__main__":
    # [
    #   [-1,  0, 0, 1],
    #   [-2, -1, 1, 2],
    #   [-2,  0, 0, 2]
    # ]
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

    # [[-2,-1,1,2],[-1,-1,1,1]]
    print(Solution().fourSum([-2, -1, -1, 1, 1, 2, 2], 0))
