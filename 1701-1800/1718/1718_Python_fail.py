from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        if n == 2:
            return [2, 1, 2]

        # 处理偶数的情况
        if n % 2 == 0:
            # [4,2,3,2,4,3,1]
            # [6,4,2,5,2,4,6,3,5,1,3]
            # [8,6,4,2,7,2,4,6,8,5,3,7,1,3,5]
            ans = []
            for i in range(n, 1, -2):
                ans.append(i)
            ans.append(n - 1)
            for i in range(2, n + 1, 2):
                ans.append(i)
            for i in range(n - 3, 1, -2):
                ans.append(i)
            ans.append(n - 1)
            for i in range(1, n - 1, 2):
                ans.append(i)
            return ans

        # 处理奇数的情况
        else:
            # [3,1,2,3,2]
            # [5,3,1,4,3,5,2,4,2]
            # [7,5,3,6,4,3,5,7,4,6,2,1,2]
            ans = []
            for i in range(n, 0, -2):
                ans.append(i)
            ans.append(n - 1)
            for i in range(3, n + 1, 2):
                ans.append(i)
            for i in range(n - 3, 1, -2):
                ans.append(i)
            ans.append(n - 1)
            for i in range(2, n - 1, 2):
                ans.append(i)
            return ans


if __name__ == "__main__":
    print(Solution().constructDistancedSequence(2))  # [2,1,2]
    print(Solution().constructDistancedSequence(3))  # [3,1,2,3,2]
    print(Solution().constructDistancedSequence(5))  # [5,3,1,4,3,5,2,4,2]
    print(Solution().constructDistancedSequence(8))  # [8,6,4,2,7,2,4,6,8,5,3,7,1,3,5]
