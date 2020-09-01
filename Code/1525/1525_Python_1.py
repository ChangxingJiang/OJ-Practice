class Solution:
    def numSplits(self, s: str) -> int:
        # 遍历统计正向到每个坐标的不同字符的数量
        nums = [0]
        now, lst = 0, set()
        for ch in s:
            if ch not in lst:
                lst.add(ch)
                now += 1
            nums.append(now)
        nums.pop()

        # 反向遍历每个坐标的不同字符数量与正向是否相同
        ans = 0
        now, lst = 0, set()
        for ch in s[::-1]:
            if ch not in lst:
                lst.add(ch)
                now += 1
            if nums.pop() == now:
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().numSplits(s="aacaba"))  # 2
    print(Solution().numSplits(s="abcd"))  # 1
    print(Solution().numSplits(s="aaaaa"))  # 4
    print(Solution().numSplits(s="acbadbaada"))  # 2
