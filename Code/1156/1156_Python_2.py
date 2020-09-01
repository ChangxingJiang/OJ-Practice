import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 统计每个字符出现的频次
        count = collections.Counter(text)

        # 将队列整理成块
        queue = []
        for ch in text:
            if not queue or ch != queue[-1][0]:
                queue.append([ch, 1])
            else:
                queue[-1][1] += 1

        ans = 0

        # 计算最长子串
        for i in range(len(queue)):
            elem = queue[i]
            length = elem[1]
            if i + 2 < len(queue):
                if queue[i + 1][1] == 1 and elem[0] == queue[i + 2][0]:
                    length += queue[i + 2][1]
            if length < count[elem[0]]:
                length += 1
            ans = max(ans, length)

        return ans


if __name__ == "__main__":
    print(Solution().maxRepOpt1(text="ababa"))  # 3
    print(Solution().maxRepOpt1(text="aaabaaa"))  # 6
    print(Solution().maxRepOpt1(text="aaabbaaa"))  # 4
    print(Solution().maxRepOpt1(text="aaaaa"))  # 5
    print(Solution().maxRepOpt1(text="abcdef"))  # 1
    print(Solution().maxRepOpt1(text="bbababaaaa"))  # 6
    print(Solution().maxRepOpt1(text="babbbbbbbbbbbbaababbaabaabaaaaaaaaabbbababba"))  # 14
