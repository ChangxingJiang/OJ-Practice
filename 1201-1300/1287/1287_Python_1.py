from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        idx = 0
        for i in range(len(arr)):
            if arr[i] != arr[idx]:
                if i - idx > len(arr) // 4:
                    return arr[idx]
                else:
                    idx = i
        else:
            return arr[idx]


if __name__ == "__main__":
    print(Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))  # 6
    print(Solution().findSpecialInteger(arr=[1, 1]))  # 1
