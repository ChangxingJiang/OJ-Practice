from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        d = (arr[-1] - arr[0]) / len(arr)

        ans = 0

        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            v = m * d + arr[0]
            if arr[m] == v:
                ans = v + d
                l = m + 1
            else:
                r = m - 1

        return int(ans)


if __name__ == "__main__":
    print(Solution().missingNumber(arr=[5, 7, 11, 13]))  # 9
    print(Solution().missingNumber(arr=[15, 13, 12]))  # 14
