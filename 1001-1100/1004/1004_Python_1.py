from typing import List


class Solution:
    def longestOnes(self, array: List[int], k: int) -> int:
        left = right = 0
        ans = 0
        now = 0
        while right < len(array):
            if array[right] == 0:
                now += 1
            while now > k:
                if array[left] == 0:
                    now -= 1
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans


if __name__ == "__main__":
    print(Solution().longestOnes(array=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))  # 6
    print(Solution().longestOnes(array=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))  # 10
    print(Solution().longestOnes(array=[0, 0, 0, 0], k=0))  # 0
