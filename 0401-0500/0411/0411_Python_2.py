from typing import List


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        s1 = len(target)

        # 计算失败列表
        # fail_list中的位是反向的
        fail_list = set()
        for word in dictionary:
            if len(word) != s1:
                continue

            same_list = []
            for j in range(s1):
                if word[j] == target[j]:
                    same_list.append(j)

            s2 = len(same_list)

            for j in range(2 ** s2):
                p1 = bin(j)[2:].zfill(s2)
                p2 = 0
                for k in range(s2):
                    if p1[k] == "1":
                        p2 |= (1 << same_list[k])
                        # p2[same_list[k]] = "1"
                fail_list.add(p2)

        if not fail_list:
            return str(len(target))

        # print(fail_list)

        ans_pattern, ans_val = target, s1

        for i in range(2 ** s1):
            if i in fail_list:
                continue
            # pattern = bin(i)[2:].zfill(s1)
            res = []
            for j in range(s1):
                if i & (1 << j):
                    # if pattern[j] == "1":
                    res.append(target[j])
                else:
                    if res and res[-1].isnumeric():
                        res[-1] = str(int(res[-1]) + 1)
                    else:
                        res.append("1")
            if len(res) < ans_val:
                ans_pattern, ans_val = "".join(res), len(res)

        return ans_pattern


if __name__ == "__main__":
    print(Solution().minAbbreviation("apple", ["blade"]))  # "a4"
    print(Solution().minAbbreviation("apple", ["plain", "amber", "blade"]))  # "1p3"
