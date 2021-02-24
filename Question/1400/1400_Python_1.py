class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = set()
        for ch in s:
            if ch not in count:
                count.add(ch)
            else:
                count.remove(ch)

        return len(count) <= k


if __name__ == "__main__":
    print(Solution().canConstruct(s="annabelle", k=2))  # True
    print(Solution().canConstruct(s="leetcode", k=3))  # False
    print(Solution().canConstruct(s="true", k=4))  # True
    print(Solution().canConstruct(s="yzyzyzyzyzyzyzy", k=2))  # True
    print(Solution().canConstruct(s="cr", k=7))  # False
