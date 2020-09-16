import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 统计每个字符出现的频次
        count = collections.Counter(text)

        # 统计最长子串
        ans = 0
        queue = []
        for ch in text:
            need_remove = []
            find = False
            for i in range(len(queue)):
                elem = queue[i]
                if ch == elem[0]:
                    elem[1] += 1
                    if not elem[2]:
                        find = True
                else:
                    if elem[2]:
                        if elem[1] < count[elem[0]]:
                            elem[1] += 1
                        ans = max(ans, elem[1])
                        need_remove.append(i)
                    else:
                        elem[2] = True
            for i in need_remove[::-1]:
                queue.pop(i)
            if not find:
                queue.append([ch, 1, False])
        for elem in queue:
            if elem[1] < count[elem[0]]:
                elem[1] += 1
            ans = max(ans, elem[1])
        return ans


if __name__ == "__main__":
    print(Solution().maxRepOpt1(text="ababa"))  # 3
    print(Solution().maxRepOpt1(text="aaabaaa"))  # 6
    print(Solution().maxRepOpt1(text="aaabbaaa"))  # 4
    print(Solution().maxRepOpt1(text="aaaaa"))  # 5
    print(Solution().maxRepOpt1(text="abcdef"))  # 1
    print(Solution().maxRepOpt1(text="bbababaaaa"))  # 6
