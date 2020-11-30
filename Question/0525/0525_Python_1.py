from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        ans = 0
        differ = 0  # 1比0多的数量
        for i, n in enumerate(nums):
            if n == 0:
                differ -= 1
            else:
                differ += 1
            if differ in hashmap:
                ans = max(ans, i - hashmap[differ])
            else:
                hashmap[differ] = i
        return ans


if __name__ == "__main__":
    print(Solution().findMaxLength([0, 1]))  # 2
    print(Solution().findMaxLength([0, 1, 0]))  # 2
