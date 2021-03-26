class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for ch in n:
            if int(ch) > ans:
                ans = int(ch)
        return ans


if __name__ == "__main__":
    print(Solution().minPartitions("32"))  # 3
    print(Solution().minPartitions("82734"))  # 8
    print(Solution().minPartitions("27346209830709182346"))  # 9
