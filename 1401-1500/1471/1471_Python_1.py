from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        size = len(arr)

        mid = arr[int((size - 1) / 2)]
        # if size % 2 == 0:
        #     mid = (arr[size // 2 - 1] + arr[size // 2]) / 2
        # else:
        #     mid = arr[size // 2]

        arr.sort(key=lambda x: (abs(x - mid), x))

        # print(mid, arr)

        return arr[-k:]


if __name__ == "__main__":
    print(Solution().getStrongest(arr=[1, 2, 3, 4, 5], k=2))  # [5,1]
    print(Solution().getStrongest(arr=[1, 1, 3, 5, 5], k=2))  # [5,5]
    print(Solution().getStrongest(arr=[6, 7, 11, 7, 6, 8], k=5))  # [11,8,6,6,7]
    print(Solution().getStrongest(arr=[6, -3, 7, 2, 11], k=3))  # [-3,11,2]
    print(Solution().getStrongest(arr=[-7, 22, 17, 3], k=2))  # [22,17]
