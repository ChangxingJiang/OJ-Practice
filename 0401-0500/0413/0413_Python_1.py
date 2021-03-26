from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        ans = 0
        d_val, d_num = A[1] - A[0], 0
        for i in range(len(A) - 1):
            d = A[i + 1] - A[i]
            if d == d_val:
                d_num += 1
                if d_num >= 2:
                    ans += d_num - 1
            else:
                d_val, d_num = d, 1

        return ans


if __name__ == "__main__":
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))  # 3
