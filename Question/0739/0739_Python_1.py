from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        size = len(T)
        ans = [0] * size
        stack = []
        for i in range(size - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
    print(Solution().dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))  # [8,1,5,4,3,2,1,1,0,0]
