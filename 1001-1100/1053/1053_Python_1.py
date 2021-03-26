from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        idx1 = -1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                idx1 = i

        if idx1 == -1:
            return arr

        idx2 = idx1 + 1
        for i in range(idx1 + 1, len(arr)):
            if arr[idx2] < arr[i] < arr[idx1]:
                idx2 = i

        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        return arr


if __name__ == "__main__":
    print(Solution().prevPermOpt1([3, 2, 1]))  # [3,1,2]
    print(Solution().prevPermOpt1([1, 1, 5]))  # [1,1,5]
    print(Solution().prevPermOpt1([1, 9, 4, 6, 7]))  # [1,7,4,6,9]
    print(Solution().prevPermOpt1([3, 1, 1, 3]))  # [1,3,1,3]
