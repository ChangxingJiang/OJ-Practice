class Solution:
    def reformatNumber(self, number: str) -> str:
        lst = [n for n in number if n.isnumeric()]

        idx, size = 0, len(lst)

        ans = []
        while size - idx > 4:
            ans.append("".join(lst[idx:idx + 3]))
            ans.append("-")
            idx += 3

        if size - idx <= 3:
            ans.append("".join(lst[idx:]))
        else:
            ans.append("".join(lst[idx:idx + 2]))
            ans.append("-")
            ans.append("".join(lst[idx + 2:]))

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().reformatNumber("1-23-45 6"))  # "123-456"
    print(Solution().reformatNumber("123 4-567"))  # "123-456"
    print(Solution().reformatNumber("123 4-5678"))  # "123-456"
    print(Solution().reformatNumber("12"))  # "123-456"
    print(Solution().reformatNumber("--17-5 229 35-39475 "))  # "123-456"
