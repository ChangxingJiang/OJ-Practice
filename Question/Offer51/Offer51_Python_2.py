from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        prefix = []
        for n in nums:
            left, right = 0, len(prefix)
            while left < right:
                mid = (left + right) // 2
                if n >= prefix[mid]:
                    left = mid + 1
                else:
                    right = mid
            ans += len(prefix) - left
            prefix[left:left] = [n]
        return ans


if __name__ == "__main__":
    print(Solution().reversePairs([7, 5, 6, 4]))  # 5
    print(Solution().reversePairs([4, 5, 6, 7]))  # 0
