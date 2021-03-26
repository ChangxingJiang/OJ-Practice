from typing import List


class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        ans = float("inf")
        for n in A:
            ans = min(ans, n)
        return 1 if sum(int(ch) for ch in str(ans)) % 2 == 0 else 0


if __name__ == "__main__":
    print(Solution().sumOfDigits([34, 23, 1, 24, 75, 33, 54, 8]))  # 0
    print(Solution().sumOfDigits([99, 77, 33, 66, 55]))  # 1
    print(Solution().sumOfDigits(
        [89, 93, 84, 87, 17, 4, 92, 26, 99, 29, 100, 85, 82, 52, 76, 27, 40, 69, 21, 92, 89, 36]))  # 1
