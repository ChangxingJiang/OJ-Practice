class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        differ = []
        for i in range(len(A)):
            if A[i] != B[i]:
                differ.append(i)

        if len(differ) == 2:
            return A[differ[0]] == B[differ[1]] and A[differ[1]] == B[differ[0]]
        elif len(differ) == 0:
            return len(set(A)) < len(A)
        else:
            return False


if __name__ == "__main__":
    print(Solution().buddyStrings("ab", "ba"))  # True
    print(Solution().buddyStrings("ab", "ab"))  # False
    print(Solution().buddyStrings("aa", "aa"))  # True
    print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))  # True
    print(Solution().buddyStrings("", "aa"))  # False
