class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # 统计连续段落：生成在不考虑通过删除中间字符使前后相连的情况下，每个连续段落中，压缩后的字符串长度以及每减少一个字符所需减少的压缩前字符数量
        lst = []  # 每减掉当前段落中的压缩后的长度需要减少的压缩前字符数量
        for i, ch in enumerate(s):
            if lst and ch == lst[-1][0]:
                lst[-1][1] += 1
                if lst[-1][1] == 2 or lst[-1][1] == 10 or lst[-1][1] == 100:
                    lst[-1].append(1)
                else:
                    lst[-1][-1] += 1
            else:
                lst.append([ch, 1, 1])

        print(lst)

        # 统计可以直接删除的段落
        before_nums, before_now = [], 0  # 压缩前前缀和
        after_nums, after_now = [], 0  # 压缩后前缀和
        hashmap = {}
        choose = []  # 可供删除段落的选择
        for i, elem in enumerate(lst):
            if elem[0] in hashmap:
                idx = hashmap[elem[0]]
                distance = before_now - before_nums[idx + 1]  # 距离之前相同字符段落的距离
                if distance <= k:
                    reduce = after_now - after_nums[idx + 1]  # 通过删除段落减少的压缩后长度
                    reduce += len(lst[idx]) + len(elem) - 4
                    reduce -= 2 if (lst[idx][1] + elem[1]) < 10 else 3
                    choose.append((idx, i, distance, reduce))  # 将结果写入到临时变量
            hashmap[elem[0]] = i
            before_nums.append(before_now)
            before_now += elem[1]
            after_nums.append(after_now)
            after_now += len(elem) - 2

        print(choose)


if __name__ == "__main__":
    print(Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2))  # 4
    print(Solution().getLengthOfOptimalCompression(s="aabbaa", k=2))  # 2
    print(Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0))  # 3
