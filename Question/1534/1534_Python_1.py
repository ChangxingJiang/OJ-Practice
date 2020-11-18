from typing import List


# 暴力解法
# O(N^3)

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    d1, d2, d3 = abs(arr[i] - arr[j]), abs(arr[j] - arr[k]), abs(arr[i] - arr[k])
                    if d1 <= a and d2 <= b and d3 <= c:
                        ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))  # 4
    print(Solution().countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))  # 0
    print(Solution().countGoodTriplets(arr=[7, 3, 7, 3, 12, 1, 12, 2, 3], a=5, b=8, c=1))  # 12
