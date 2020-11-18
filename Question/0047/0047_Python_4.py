from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def track_back(now_idx):
            if now_idx == n - 1:
                self.ans.append(nums[:])
            tmp_set = set()
            for i in range(now_idx, n):
                # 剪枝条件
                if nums[i] in tmp_set:
                    continue
                tmp_set.add(nums[i])

                nums[i], nums[now_idx] = nums[now_idx], nums[i]
                track_back(now_idx + 1)
                nums[i], nums[now_idx] = nums[now_idx], nums[i]

        track_back(0)

        return self.ans


if __name__ == "__main__":
    # [
    #   [1,1,2],
    #   [1,2,1],
    #   [2,1,1]
    # ]
    print(Solution().permuteUnique([1, 1, 2]))
