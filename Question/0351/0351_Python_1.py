class Solution:
    def __init__(self):
        self.used = [False] * 9

    def numberOfPatterns(self, m: int, n: int) -> int:
        return self.dfs(-1, m, n)

    def dfs(self, now, m, n):
        m = m - 1 if m > 0 else 0
        n -= 1

        next_list = self.get_next(now)

        if m == 0:
            ans = len(next_list)
        else:
            ans = 0

        if n == 0:
            # print("now:" + str(now), "m:" + str(m + 1), "n:" + str(n + 1), ":", len(next_list))
            return len(next_list)
        else:
            for next in next_list:
                self.used[next] = True
                ans += self.dfs(next, m, n)
                self.used[next] = False
            # print("now:" + str(now), "m:" + str(m + 1), "n:" + str(n + 1), ":", ans,
            #       "(", len(next_list) if m == 0 else 0, ")")
            return ans

    def get_next(self, now):
        """寻找所有可能的下一个位置"""
        val = [i for i in range(9) if self.is_valid(now, i)]
        # print("now:" + str(now), "used:", self.used, "->", val)
        return val

    def is_valid(self, start, end):
        """判断移动是否有效"""
        if self.used[end]:
            return False
        if start == -1:
            return True
        if start > end:
            start, end = end, start
        if start == 0:
            if end == 2:
                return self.used[1]
            if end == 6:
                return self.used[3]
            if end == 8:
                return self.used[4]
            return True
        if start == 1:
            if end == 7:
                return self.used[4]
            return True
        if start == 2:
            if end == 6:
                return self.used[4]
            if end == 8:
                return self.used[5]
            return True
        if start == 3:
            if end == 5:
                return self.used[4]
            return True
        if start == 6:
            if end == 8:
                return self.used[7]
            return True
        return True


if __name__ == "__main__":
    print(Solution().numberOfPatterns(m=1, n=1))  # 9
    print(Solution().numberOfPatterns(m=1, n=2))  # 65
