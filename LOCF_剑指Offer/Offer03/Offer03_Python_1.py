from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return n
            hashmap.add(n)


if __name__ == "__main__":
    # 2或3
    print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
