from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 2:
            return arr

        change = True
        while change:
            change = False
            new = [arr[0]]
            for i in range(1, len(arr) - 1):
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new.append(arr[i] - 1)
                    change = True
                elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new.append(arr[i] + 1)
                    change = True
                else:
                    new.append(arr[i])
            new.append(arr[-1])
            arr = new

        return arr


if __name__ == "__main__":
    print(Solution().transformArray([6, 2, 3, 4]))  # [6,3,3,4]
    print(Solution().transformArray([1, 6, 3, 4, 3, 5]))  # [1,4,4,4,4,5]
