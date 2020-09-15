import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contain():
            for a in aim:
                if a not in count or count[a] < aim[a]:
                    return False
            return True

        N = len(s)
        aim = collections.Counter(t)

        ans = None

        left = right = 0  # 窗口左侧和窗口右侧的坐标
        count = collections.Counter()  # 当前窗口内各所需字母数量
        while right < N:
            ch = s[right]
            if ch in aim:  # 更新窗口内字母数量
                count[ch] += 1
            while left <= right and (s[left] not in aim or count[s[left]] > aim[s[left]]):  # 更新窗口左侧边缘位置
                if count[s[left]] > aim[s[left]]:
                    count[s[left]] -= 1
                left += 1

            right += 1
            # print(left, right, "[", ch, "]", "->", count)

            # 判断当前结果是否为最小覆盖子串
            if contain():
                if not ans or right - left - 1 < len(ans):
                    ans = s[left:right]

        return ans if ans else ""


if __name__ == "__main__":
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))  # "BANC"
    print(Solution().minWindow(s="A", t="AA"))  # ""
    print(Solution().minWindow(s="AB", t="B"))  # "B"
