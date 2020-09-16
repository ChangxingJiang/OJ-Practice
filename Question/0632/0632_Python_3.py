import collections
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 生成包含序列
        num_count = collections.defaultdict(list)
        for i, num in enumerate(nums):
            for n in num:
                num_count[n].append(i)

        # 依据值排序序列
        idxs = sorted(num_count.keys())

        ans = [idxs[0], idxs[-1]]
        left = 0
        count = collections.Counter()
        need = len(nums)
        for right in idxs:
            for n in num_count[right]:
                count[n] += 1
                if count[n] == 1:
                    need -= 1
            if need == 0:
                while need == 0:
                    for n in num_count[idxs[left]]:
                        count[n] -= 1
                        if count[n] == 0:
                            need += 1
                    left += 1
                if right - idxs[left - 1] < ans[1] - ans[0]:
                    ans = [idxs[left - 1], right]

        return ans


if __name__ == "__main__":
    print(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))  # [20,24]
    print(Solution().smallestRange([[-5, -4, -3, -2, -1], [1, 2, 3, 4, 5]]))  # [-1,1]
