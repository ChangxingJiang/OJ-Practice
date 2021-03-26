class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()

        def dfs(now, surplus):
            if now:
                ans.add(now)
            if surplus:
                for i, ch in enumerate(surplus):
                    dfs(now + ch, surplus[:i] + surplus[i + 1:])

        dfs("", tiles)

        return len(ans)


if __name__ == "__main__":
    print(Solution().numTilePossibilities("AAB"))  # 8
    print(Solution().numTilePossibilities("AAABBC"))  # 188
