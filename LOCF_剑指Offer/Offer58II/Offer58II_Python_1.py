class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        n %= len(s)
        return s[n:] + s[:n]


if __name__ == "__main__":
    print(Solution().reverseLeftWords("abcdefg", 2))  # "cdefgab"
    print(Solution().reverseLeftWords("lrloseumgh", 6))  # "umghlrlose"
