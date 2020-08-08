from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        ans = 0
        while A:
            ans += sum(A)
            ans = ans % (10 ** 9 + 7)
            B = []
            for i in range(len(A) - 1):
                B.append(min(A[i], A[i + 1]))
            A = B
        return ans


if __name__ == "__main__":
    print(Solution().sumSubarrayMins([3, 1, 2, 4]))  # 17
    print(Solution().sumSubarrayMins([85]))  # 85
