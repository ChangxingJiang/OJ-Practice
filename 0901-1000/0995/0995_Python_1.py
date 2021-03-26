from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:
        # 处理K=1的特殊情况
        if k == 1:
            return A.count(0)

        size = len(A)
        array = [0] * (size + 1)
        ans = 0
        now = 0
        for i in range(size):
            now ^= array[i]
            # print(i, ":", now, "->", now ^ A[i], array)
            if i < size - k + 1:
                if now ^ A[i] == 0:
                    now ^= 1
                    array[i + k] = 1
                    ans += 1
            else:
                if now ^ A[i] == 0:
                    return -1

        return ans


if __name__ == "__main__":
    print(Solution().minKBitFlips(A=[0, 1, 0], k=1))  # 2
    print(Solution().minKBitFlips(A=[1, 1, 0], k=2))  # -1
    print(Solution().minKBitFlips(A=[0, 0, 0, 1, 0, 1, 1, 0], k=3))  # 3
