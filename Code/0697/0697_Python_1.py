from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        maximum = max(hashmap.values())

        max_nums = []
        for key, value in hashmap.items():
            if value == maximum:
                max_nums.append(key)

        minimum = len(nums)
        for max_num in max_nums:
            idx1 = 0
            idx2 = len(nums) - 1
            while nums[idx1] != max_num:
                idx1 += 1
            while nums[idx2] != max_num:
                idx2 -= 1
            size = idx2 - idx1 + 1
            minimum = min(minimum, size)

        return minimum


if __name__ == "__main__":
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))  # 2
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))  # 6
