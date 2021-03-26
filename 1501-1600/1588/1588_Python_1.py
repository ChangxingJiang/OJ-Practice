from typing import List


# O(N^3)


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for length in range(1, min(101, len(arr) + 1), 2):
            for i in range(len(arr) - length + 1):
                ans += sum(arr[i:i + length])
        return ans


if __name__ == "__main__":
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))  # 58
    print(Solution().sumOddLengthSubarrays([1, 2]))  # 3
    print(Solution().sumOddLengthSubarrays([10, 11, 12]))  # 66
