from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if target in arr:
            return arr.index(target)
        else:
            return -1


if __name__ == "__main__":
    # 8
    print(Solution().search(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5))

    # -1
    print(Solution().search(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=11))

    # 5
    print(Solution().search(arr=[1, 1, 1, 1, 1, 2, 1, 1, 1], target=2))

    # 0
    print(Solution().search(arr=[5, 5, 5, 1, 2, 3, 4, 5], target=5))
