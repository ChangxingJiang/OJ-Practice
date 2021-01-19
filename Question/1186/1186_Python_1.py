from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = -10001
        a = b = -10001
        for n in arr:
            a, b = max(a + n, n), max(b + n, a)
            ans = max(ans, a, b)
        return ans


if __name__ == "__main__":
    print(Solution().maximumSum(arr=[1, -2, 0, 3]))  # 4
    print(Solution().maximumSum(arr=[1, -2, -2, 3]))  # 3
    print(Solution().maximumSum(arr=[-1, -1, -1, -1]))  # -1
