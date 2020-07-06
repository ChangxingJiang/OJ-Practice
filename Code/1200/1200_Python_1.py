from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_num = float("inf")
        min_list = []
        for i in range(len(arr) - 1):
            d = arr[i + 1] - arr[i]
            if d < min_num:
                min_num = d
                min_list = [[arr[i], arr[i + 1]]]
            elif d == min_num:
                min_list.append([arr[i], arr[i + 1]])
        return min_list


if __name__ == "__main__":
    print(Solution().minimumAbsDifference(arr=[4, 2, 1, 3]))  # [[1,2],[2,3],[3,4]]
    print(Solution().minimumAbsDifference(arr=[1, 3, 6, 10, 15]))  # [[1,3]]
    print(Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]))  # [[-14,-10],[19,23],[23,27]]
