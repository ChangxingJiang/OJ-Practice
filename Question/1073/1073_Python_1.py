from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        arr1.reverse()
        arr2.reverse()

        for i in range(len(arr2)):
            arr1[i] += arr2[i]

        arr1.extend([0, 0, 0])
        i = 0
        while i < len(arr1):
            if arr1[i] >= 2:
                v = arr1[i] // 2
                arr1[i] %= 2
                arr1[i + 1] -= v
            elif arr1[i] <= -1:
                arr1[i] *= -1
                arr1[i + 1] += arr1[i]
            i += 1

        while arr1 and arr1[-1] == 0:
            arr1.pop()

        arr1.reverse()

        return arr1 if len(arr1) > 0 else [0]


if __name__ == "__main__":
    print(Solution().addNegabinary(arr1=[1, 1, 1, 1, 1], arr2=[1, 0, 1]))  # [1,0,0,0,0]
    print(Solution().addNegabinary(arr1=[1], arr2=[1, 1]))  # [1,0,0,0,0]
    print(Solution().addNegabinary(arr1=[0], arr2=[0]))  # [1,0,0,0,0]
    print(Solution().addNegabinary(arr1=[1], arr2=[1]))  # [1,1,0]
    print(Solution().addNegabinary(arr1=[1, 0, 1], arr2=[1, 0, 1]))  # [1,1,1,1,0]
