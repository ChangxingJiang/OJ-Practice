class Solution:
    def reorganizeString(self, S: str) -> str:
        # 统计每个字母的出现频次
        count = [(S.count(x), x) for x in set(S)]

        # 计算是否可以构成字符串
        if max(count, key=lambda k: k[0])[0] > (len(S) + 1) / 2:
            return ""

        # 构成临时字符串
        count.sort(key=lambda k: k[0])
        nums = []
        for num, x in count:
            nums += [x] * num

        # # 生成结果字符串
        ans = []
        i1 = 0
        i2 = int(len(S) / 2)
        first = True
        for i in range(len(S)):
            if first:
                ans.append(nums[i2])
                i2 += 1
            else:
                ans.append(nums[i1])
                i1 += 1
            first = not first

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().reorganizeString(S="aab"))  # "aba"
    print(Solution().reorganizeString(S="aaab"))  # ""
