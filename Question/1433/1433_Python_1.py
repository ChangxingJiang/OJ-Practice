class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        n = len(s1)
        direction = None
        for i in range(n):
            if s1[i] < s2[i]:
                if direction is None:
                    direction = False
                elif direction:
                    return False
            elif s1[i] > s2[i]:
                if direction is None:
                    direction = True
                elif not direction:
                    return False
        return True


if __name__ == "__main__":
    print(Solution().checkIfCanBreak(s1="abc", s2="xya"))  # True
    print(Solution().checkIfCanBreak(s1="abe", s2="acd"))  # False
    print(Solution().checkIfCanBreak(s1="leetcodee", s2="interview"))  # True
