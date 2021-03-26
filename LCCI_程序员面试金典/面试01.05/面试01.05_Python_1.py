class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        N1, N2 = len(first), len(second)
        if N1 == N2:
            diff = False
            for i in range(N1):
                if first[i] != second[i]:
                    if diff:
                        return False
                    else:
                        diff = True
            return True
        elif N1 == N2 - 1:
            diff = 0
            i = 0
            while i < N1:
                if first[i] != second[i + diff]:
                    if diff:
                        return False
                    else:
                        diff += 1
                else:
                    i += 1
            return True
        elif N2 == N1 - 1:
            diff = 0
            i = 0
            while i < N2:
                if first[i + diff] != second[i]:
                    if diff:
                        return False
                    else:
                        diff += 1
                else:
                    i += 1
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().oneEditAway("pale", "ple"))  # True
    print(Solution().oneEditAway("pales", "pal"))  # False
    print(Solution().oneEditAway("teacher", "bleacher"))  # False
