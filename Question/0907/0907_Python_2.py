from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        now = 0
        ans = 0  # 当前累加总和
        for i in range(len(A)):
            n = A[i]
            v = 1
            while stack and stack[-1][0] >= n:
                s = stack.pop()
                now -= s[0] * s[1]
                v += s[1]
            now += n * v
            stack.append([n, v])
            ans += now
            ans = ans % (10 ** 9 + 7)
        return ans


if __name__ == "__main__":
    print(Solution().sumSubarrayMins([3, 1, 2, 4]))  # 17
    print(Solution().sumSubarrayMins([85]))  # 85
