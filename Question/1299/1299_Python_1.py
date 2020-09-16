from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        now = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], now = now, max(now, arr[i])
        return arr


if __name__ == "__main__":
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))  # [18,6,6,6,1,-1]
