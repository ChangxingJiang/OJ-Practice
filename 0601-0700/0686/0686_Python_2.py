class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if not set(B).issubset(set(A)):
            return -1
        size = len(B) // len(A)
        for i in range(size, size + 3):
            if B in A * i:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().repeatedStringMatch("abcd", "cdabcdab"))  # 3
    print(Solution().repeatedStringMatch("a", "aa"))  # 2
