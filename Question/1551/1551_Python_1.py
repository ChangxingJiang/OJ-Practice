# O(1)
# 数学


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        if n % 2 == 0:
            ans += n // 2
            n -= 1

        n -= 1
        n //= 2

        ans += (n + 1) * n

        return ans


if __name__ == "__main__":
    print(Solution().minOperations(3))  # 2
    print(Solution().minOperations(6))  # 9
