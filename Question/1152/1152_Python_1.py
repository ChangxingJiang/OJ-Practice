import collections
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        size1 = len(username)

        # 依据用户整理
        # O(N)
        count1 = collections.defaultdict(list)
        for i in range(size1):
            user, time, site = username[i], timestamp[i], website[i]
            count1[user].append((time, site))

        count2 = collections.defaultdict(list)
        for user, lst in count1.items():
            count2[user] = [i[1] for i in sorted(lst)]

        # 依据路径整理
        count3 = collections.Counter()
        for lst in count2.values():
            paths = set()
            size2 = len(lst)
            for i in range(size2):
                for j in range(i + 1, size2):
                    for k in range(j + 1, size2):
                        paths.add((lst[i], lst[j], lst[k]))
            # 每个用户去重
            for path in paths:
                count3[path] += 1

        # 返回结果
        ans = list(count3.keys())
        ans.sort(key=lambda x: (-count3[x], x))

        return list(ans[0])


if __name__ == "__main__":
    # ["home","about","career"]
    print(Solution().mostVisitedPattern(
        username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]))

    # ["y","y","loedo"]
    print(Solution().mostVisitedPattern(["dowg", "dowg", "dowg"],
                                        [158931262, 562600350, 148438945],
                                        ["y", "loedo", "y"]))
