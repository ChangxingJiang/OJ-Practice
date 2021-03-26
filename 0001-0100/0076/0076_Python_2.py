import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        surplus = len(t)  # 当前剩余尚未覆盖的字母数
        count = collections.defaultdict(int)
        for ch in t:
            count[ch] += 1

        ans = (0, float("inf"))

        left = 0  # 窗口左侧和窗口右侧的坐标
        for right, rch in enumerate(s):
            # 更新窗口内字母数量
            if count[rch] > 0:
                surplus -= 1
            count[rch] -= 1

            if surplus == 0:
                # 更新窗口左侧边缘位置
                while True:
                    lch = s[left]
                    if count[lch] == 0:
                        break
                    count[lch] += 1
                    left += 1

                # 判断当前结果是否为最小覆盖子串
                if right - left < ans[1] - ans[0]:
                    ans = (left, right)

                # 再向后移动左侧边缘，等待重新满足条件的情况
                count[s[left]] += 1
                surplus += 1
                left += 1

        return s[ans[0]:ans[1] + 1] if ans[1] < len(s) else ""


if __name__ == "__main__":
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))  # "BANC"
    print(Solution().minWindow(s="A", t="AA"))  # ""
    print(Solution().minWindow(s="AB", t="B"))  # "B"
    print(Solution().minWindow(s="abcabdebac", t="cea"))  # ""ebac""
