from typing import List


class Solution:
    def restoreIpAddresses(self, s: str, num: int = 4) -> List[str]:
        N = len(s)

        # 处理长度异常的情况
        if N < num or N > num * 3:
            return []

        # 处理最后一段的情况
        if num == 1:
            n = int(s)
            if 1 <= n <= 255 and s[0] != "0":
                return [s]
            elif n == 0 and len(s) == 1:
                return [s]
            else:
                return []

        # 处理第一个数字为0的情况
        if s[0] == "0":
            return [s[:1] + "." + ss for ss in self.restoreIpAddresses(s[1:], num - 1)] if N <= num * 3 - 2 else []

        # 处理其他情况
        lst1 = [s[:1] + "." + ss for ss in self.restoreIpAddresses(s[1:], num - 1)] if N <= num * 3 - 2 else []
        lst2 = [s[:2] + "." + ss for ss in self.restoreIpAddresses(s[2:], num - 1)] if num + 1 <= N <= num * 3 - 1 else []
        lst3 = [s[:3] + "." + ss for ss in self.restoreIpAddresses(s[3:], num - 1)] if num + 2 <= N and int(s[0:3]) <= 255 else []
        return lst1 + lst2 + lst3


if __name__ == "__main__":
    print(Solution().restoreIpAddresses("25525511135"))  # ["255.255.11.135", "255.255.111.35"]
    print(Solution().restoreIpAddresses("010010"))  # ["0.10.0.10","0.100.1.0"]
    print(Solution().restoreIpAddresses("00000"))  # []
