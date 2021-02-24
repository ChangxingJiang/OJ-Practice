from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = 0, max(arr)

        while left < right:
            mid = (left + right) // 2

            res = sum([n if n <= mid else mid for n in arr])

            if res < target:
                left = mid + 1
            elif res > target:
                right = mid
            else:
                return mid

        res1 = sum([n if n <= (left - 1) else (left - 1) for n in arr])
        res2 = sum([n if n <= left else left for n in arr])

        if abs(res1 - target) > abs(res2 - target):
            return left
        else:
            return left - 1


if __name__ == "__main__":
    print(Solution().findBestValue(arr=[4, 9, 3], target=10))  # 3
    print(Solution().findBestValue(arr=[2, 3, 5], target=10))  # 5
    print(Solution().findBestValue(arr=[2, 3, 5], target=11))  # 5
    print(Solution().findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803))  # 11361
