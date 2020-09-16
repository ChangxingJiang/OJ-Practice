class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) == 0 and len(B) == 0:
            return True
        elif len(A) == 0 or len(B) == 0:
            return False

        b = B[0]
        if b not in A:
            return False
        start = 0
        while start < len(A):
            s = A[start:]
            if b not in s:
                break

            idx = s.index(b) + start
            if B == A[idx:] + A[0:idx]:
                return True
            start = idx + 1

        return False


if __name__ == "__main__":
    print(Solution().rotateString(A='abcde', B='cdeab'))  # True
    print(Solution().rotateString(A='abcde', B='abced'))  # False
