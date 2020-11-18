from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 计算所有字母的第一个位置和最后一个位置
        # O(S)
        positions = [[-1, -1]] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if positions[idx] == [-1, -1]:
                positions[idx] = [i, i]
            else:
                positions[idx][1] = i

        # 过滤不存在的字母
        # O(26) = O(1)
        positions = [(chr(97 + i), position[0], position[1]) for i, position in enumerate(positions) if
                     position != [-1, -1]]

        maybe_ans = set()

        while positions:
            # 计算所有不存在重叠的情况
            # O(26×26)
            for ch1, left1, right1 in positions:
                # 相邻必定内部无其他重叠的情况
                if left1 == right1 or left1 == right1 - 1:
                    maybe_ans.add((ch1, left1, right1))
                    continue

                # 不相邻判断是否有重叠
                for ch2, left2, right2 in positions:
                    if left1 < left2 < right1 or left1 < right2 < right1 or left2 < left1 < right1 < right2:
                        break
                else:
                    maybe_ans.add((ch1, left1, right1))

            # 过滤剩余的条件（过滤内部已经包含其他不存在重叠的情况，因为内部的一定更短）
            # O(26×26)
            filter_positions = []
            for ch1, left1, right1 in positions:
                if (ch1, left1, right1) in maybe_ans:
                    continue

                for ch2, left2, right2 in maybe_ans:
                    if left1 < left2 < right1 or left1 < right2 < right1:
                        break
                else:
                    filter_positions.append((ch1, left1, right1))

            positions = filter_positions

            # 处理包含式重叠的情况
            remove_list = set()
            for ch1, left1, right1 in positions:
                for ch2, left2, right2 in positions:
                    if left1 < left2 < right2 < right1:
                        if ch1 in s[left2:right2 + 1]:
                            remove_list.add((ch2, left2, right2))
                        else:
                            remove_list.add((ch1, left1, right1))

            positions = [position for position in positions if position not in remove_list]

            # 处理交叉式重叠的情况
            new_list = set()

            print(positions)



if __name__ == "__main__":
    print(Solution().maxNumOfSubstrings(s="adefaddaccc"))  # ["e","f","ccc"]
    print(Solution().maxNumOfSubstrings(s="abbaccd"))  # ["d","bb","cc"]
    print(Solution().maxNumOfSubstrings(s="ababad"))  # ["ababa","d"]
    print(Solution().maxNumOfSubstrings(s="ababd"))  # ["abab","d"]
    print(Solution().maxNumOfSubstrings(s="cabcabd"))  # ["cabcab","d"]
