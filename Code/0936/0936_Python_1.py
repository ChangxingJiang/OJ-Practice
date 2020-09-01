import re
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # 生成正则表达式
        S = len(stamp)
        if S == 1:
            regex = stamp
            repl = "#"
        else:
            regex = []
            for i in range(0, S):
                tmp = []
                for j in range(0, S):
                    if j != i:
                        tmp.append("[#" + stamp[j] + "]")
                    else:
                        tmp.append(stamp[j])
                regex.append("".join(tmp))
            regex = "|".join(regex)
            repl = "#" * S

        # 计算印制顺序
        ans = []
        while True:
            match = re.search(regex, target)
            if match:
                i1 = match.span()[0]
                i2 = match.span()[1]
                target = target[:i1] + repl + target[i2:]
                ans.append(i1)
            else:
                break

        # 判断印制是否成功
        if target.count("#") == len(target):
            return list(reversed(ans))
        else:
            return []


if __name__ == "__main__":
    print(Solution().movesToStamp(stamp="abc", target="ababc"))  # [0,2]
    print(Solution().movesToStamp(stamp="abca", target="aabcaca"))  # [3,0,1]
    print(Solution().movesToStamp(stamp="zbs", target="zbzbsbszbssbzbszbsss"))  # [11,9,17,10,6,5,3,1,16,14,13,8,4,0,15,12,7,2]
