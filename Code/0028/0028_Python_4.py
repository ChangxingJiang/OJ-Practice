class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next_val(t):
            """通过计算返回子串t的next数组"""
            i = 0
            j = -1
            next = [-1] * len(t)
            while i < len(t) - 1:
                if j == -1 or t[i] == t[j]:
                    i += 1
                    j += 1
                    if t[i] != t[j]:
                        next[i] = j
                    else:
                        next[i] = next[j]
                else:
                    j = next[j]  # 若字符不相同，则j值回溯
            return next

        i = 0  # i用于主串s中当前位置下标，若pos不为1则从pos位置开始匹配
        j = 0  # j用于子串t中当前位置下标值
        next = get_next_val(needle)
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j >= len(needle):
            return i - len(needle)
        else:
            return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))  # 2
    print(Solution().strStr("aaaaa", "bba"))  # -1
    print(Solution().strStr("hello", ""))  # 0
    print(Solution().strStr("mississippi", "issip"))  # 4
