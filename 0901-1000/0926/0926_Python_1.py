class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        lst1 = [0]
        for ch in S:
            if ch == "1":
                lst1.append(lst1[-1] + 1)
            else:
                lst1.append(lst1[-1])

        lst2 = [0]
        for ch in S[::-1]:
            if ch == "0":
                lst2.append(lst2[-1] + 1)
            else:
                lst2.append(lst2[-1])
        lst2.reverse()

        ans = len(S)
        for i in range(len(lst1)):
            ans = min(ans, lst1[i] + lst2[i])
        return ans


if __name__ == "__main__":
    print(Solution().minFlipsMonoIncr("00110"))  # 1
    print(Solution().minFlipsMonoIncr("010110"))  # 2
    print(Solution().minFlipsMonoIncr("00011000"))  # 2
