from functools import cache


class Solution:
    def is_neighbour(self, ch1, ch2):
        if (abs(ord(ch1) - ord(ch2))) == 1:
            return True
        return ch1 == "a" and ch2 == "z" or ch1 == "z" and ch2 == "a"

    def lexicographicallySmallestString(self, s: str) -> str:
        @cache
        def is_maybe_empty(i, j):
            """判断 s[i:j] 是否可以被操作为空"""
            if i == j:
                return True  # 已经是空字符串
            if (j - i) % 2 != 0:
                return False  # 长度不是偶数
            if self.is_neighbour(s[i], s[j - 1]):
                if is_maybe_empty(i + 1, j - 1):
                    return True
            for k in range(i + 2, j, 2):
                if is_maybe_empty(i, k) and is_maybe_empty(k, j):
                    return True
            return False

        @cache
        def dfs(i) -> str:
            """广度优先搜索，返回 s[i:] 之后的最小字典序"""
            if i == len(s):
                return ""

            # 选择当前节点
            choose = s[i] + dfs(i + 1)

            for j in range(i + 1, len(s) + 1):
                # print(f"is_maybe_mepty: ({i}, {j}) -> {is_maybe_empty(i, j)}")
                if is_maybe_empty(i, j):
                    choose_2 = dfs(j)
                    if choose_2 < choose:
                        choose = choose_2

            return choose

        return dfs(0)


if __name__ == "__main__":
    print(Solution().lexicographicallySmallestString(s="abc"))  # "a"
    print(Solution().lexicographicallySmallestString(s="bcda"))  # ""
    print(Solution().lexicographicallySmallestString(s="zdce"))  # "zdce"
