from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, arr: List[int], s1: int, s2: int) -> int:
        size = len(arr)
        for i in range(1, size):
            arr[i] += arr[i - 1]

        ans, max1, max2 = arr[s1 + s2 - 1], arr[s1 - 1], arr[s2 - 1]

        for i in range(s1 + s2, size):
            max1 = max(max1, arr[i - s2] - arr[i - s1 - s2])  # 最后s2个留给s2，前面求s1最大值
            max2 = max(max2, arr[i - s1] - arr[i - s1 - s2])  # 最后s1个留给s1，前面求s2最大值
            ans = max(ans,
                      max1 + arr[i] - arr[i - s2],
                      max2 + arr[i] - arr[i - s1])

        return ans


if __name__ == "__main__":
    print(Solution().maxSumTwoNoOverlap(arr=[0, 6, 5, 2, 2, 5, 1, 9, 4], s1=1, s2=2))  # 20
    print(Solution().maxSumTwoNoOverlap(arr=[3, 8, 1, 3, 2, 1, 8, 9, 0], s1=3, s2=2))  # 29
    print(Solution().maxSumTwoNoOverlap(arr=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], s1=4, s2=3))  # 31
