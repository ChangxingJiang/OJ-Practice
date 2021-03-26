from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr) - 2):
            if arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]:
                return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().canMakeArithmeticProgression(arr=[3, 5, 1]))  # True
    print(Solution().canMakeArithmeticProgression(arr=[1, 2, 4]))  # False
