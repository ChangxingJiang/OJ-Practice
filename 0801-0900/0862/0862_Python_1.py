from typing import List
import collections

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)

        # 计算前序和
        B = [0]  # 前序和
        for n in A:
            B.append(B[-1] + n)

        #  移动窗口计算最小值
        ans = N + 1
        queue = collections.deque()
        for i,n in enumerate(B):
            while queue and n <= B[queue[-1]]:
                queue.pop()
            while queue and n - B[queue[0]] >= K:
                t = queue.popleft()
                ans = min(ans, i - t)
            queue.append(i)
        return ans if ans < N + 1 else -1


if __name__ == "__main__":
    print(Solution().shortestSubarray(A=[1], K=1))  # 1
    print(Solution().shortestSubarray(A=[1, 2], K=4))  # -1
    print(Solution().shortestSubarray(A=[2, -1, 2], K=3))  # 3
    print(Solution().shortestSubarray(A=[84, -37, 32, 40, 95], K=167))  # 3
    print(Solution().shortestSubarray(A=[56, -21, 56, 35, -9], K=61))  # 2
