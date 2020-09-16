from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop(-1)


if __name__ == "__main__":
    param = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(param)
    print(param)  # [1,0,0,2,3,0,0,4]

    param = [1, 2, 3]
    Solution().duplicateZeros(param)
    print(param)  # [1,2,3]
