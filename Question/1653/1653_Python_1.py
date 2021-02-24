class Solution:
    def minimumDeletions(self, s: str) -> int:
        size = len(s)

        lst1 = [0] * (size + 1)  # 左侧b的数量
        lst2 = [0] * (size + 1)  # 右侧a的数量

        for i in range(size):
            if s[i] == "b":
                lst1[i + 1] = lst1[i] + 1
            else:
                lst1[i + 1] = lst1[i]

        for i in range(size - 1, -1, -1):
            if s[i] == "a":
                lst2[i] = lst2[i + 1] + 1
            else:
                lst2[i] = lst2[i + 1]

        ans = size
        for i in range(size + 1):
            ans = min(ans, lst1[i] + lst2[i])
        return ans


if __name__ == "__main__":
    print(Solution().minimumDeletions(s="aababbab"))  # 2
    print(Solution().minimumDeletions(s="bbaaaaabb"))  # 2
