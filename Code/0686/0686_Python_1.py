class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = len(B) // len(A) + 2
        n = A * times
        if B in n:
            n = A * (times - 1)
            if B in n:
                n = A * (times - 2)
                if B in n:
                    return times - 2
                else:
                    return times - 1
            else:
                return times
        else:
            return -1


if __name__ == "__main__":
    print(Solution().repeatedStringMatch("abcd", "cdabcdab"))  # 3
    print(Solution().repeatedStringMatch("a", "aa"))  # 2
