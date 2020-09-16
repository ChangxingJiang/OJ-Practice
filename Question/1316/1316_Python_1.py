class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        ans = set()
        for i in range(N):
            for j in range(1, (N - i) // 2 + 1):
                if text[i:i + j] == text[i + j:i + 2 * j]:
                    ans.add(text[i:i + 2 * j])
        return len(ans)


if __name__ == "__main__":
    print(Solution().distinctEchoSubstrings(text="abcabcabc"))  # 3
    print(Solution().distinctEchoSubstrings(text="leetcodeleetcode"))  # 2
