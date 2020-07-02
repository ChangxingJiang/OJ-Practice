class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B:
            return len(set(A)) < len(A)
        else:
            if len(A) != len(B):
                return False
            differ = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    differ.append(i)
            return len(differ) == 2 and A[differ[0]] == B[differ[1]] and A[differ[1]] == B[differ[0]]


if __name__ == "__main__":
    print(Solution().buddyStrings("ab", "ba"))  # True
    print(Solution().buddyStrings("ab", "ab"))  # False
    print(Solution().buddyStrings("aa", "aa"))  # True
    print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))  # True
    print(Solution().buddyStrings("", "aa"))  # False
