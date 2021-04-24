# 测试用例94/101未通过

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        size1, size2 = len(word1), len(word2)

        ans = []

        i1, i2 = 0, 0  # 当前已移动的位置
        j1, j2 = 0, 0  # 当前已比较的位置

        while j1 < size1 and j2 < size2:
            print(ans, ":", i1, word1[i1:], j1, ";", i2, word2[i2:], j2)
            if i1 < j1:
                # 当前两字符串的开头均小于相同序列的开头
                if word1[i1] > word1[j1] and word1[i1] > word2[j2]:
                    ans.append(word1[i1:j1] * 2)
                    i1, i2 = j1, j2

                # 某一字符串的开头小于相同序列的开头
                elif word1[i1] > word1[j1]:  # 移动串2的相同序列
                    ans.append(word2[i2:j2])
                    j1 = i1
                    i2 = j2
                elif word1[i1] > word2[j2]:  # 移动串1的相同序列
                    ans.append(word1[i1:j1])
                    j2 = i2
                    i1 = j1

                # now[0] <= word1[0] and now[0] <= word2[0]
                elif word1[j1] > word2[j2]:  # 移动串1的相同序列
                    ans.append(word1[i1:j1])
                    j2 = i2
                    i1 = j1
                elif word1[j1] < word2[j2]:  # 移动串2的相同序列
                    ans.append(word2[i2:j2])
                    j1 = i1
                    i2 = j2

                else:  # now[0] <= word1[0] == word2[0]
                    j1 += 1
                    j2 += 1

            else:
                if word1[i1] > word2[i2]:
                    ans.append(word1[i1])
                    i1 += 1
                    j1 += 1
                elif word1[i1] < word2[i2]:
                    ans.append(word2[i2])
                    i2 += 1
                    j2 += 1

                else:  # word1[0] == word2[0]
                    j1 += 1
                    j2 += 1

            if ans and ans[-1] == "jujj":
                break

        print(ans)

        # 两个字符串到结尾都完全相同
        if i1 == size1 and i2 == size2:
            ans.append(word1[i1:])
            ans.append(word2[i2:])

        # 两字符串有一个比较到结尾，但长度不相同
        else:
            ans.append(max(word1[i1:] + word2[i2:], word2[i2:] + word1[i1:]))

        return "".join(ans)


if __name__ == "__main__":
    # "cbcabaaaaa"
    print(Solution().largestMerge(word1="cabaa", word2="bcaaa"))

    # "abdcabcabcaba"
    print(Solution().largestMerge(word1="abcabc", word2="abdcaba"))

    # 测试用例 90/101
    # "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"
    print(Solution().largestMerge(word1="uuurruuuruuuuuuuuruuuuu",
                                  word2="urrrurrrrrrrruurrrurrrurrrrruu"))

    # 测试用例 97/101
    print(Solution().largestMerge(
        word1="uuuuuuuuujuujuuuuuuuujuuuuuuuujujuuuuuuujuuuuuuuuuuuujuuujujjuujuuuuuuuuuuuuuuuujuuuuuuuuuuuuuuuuujujuuuuuuuuuuuuuuuuuujuuuujuuuujuuuuujuuuujuuuujuuuuuuuuuujujuuuuujujuuuujjujuujjuuuuuuujujjuuujjjjjuuujuujjuujujujuujuujujuujuuuujuuuuuuuuuuuuuuuuuuuujjuuuuuujuuuuuuuuuuuuuuuuuujujuuuuuuujujjuuuuuuuuujuuuuuuuuujuuujujjjjujjuuuuujuuuuuuujuuuuuuuuuuuujjuuuuuuuuuuujuuuujuujjuuuujuuuujuuuuuuuuuuuujjuuuuuuuujuujuuuuujuuuuuuuuuujjuuuuuuuujuuujjuuuuuuujuujjjuuuuujuuujujuuuuuuuuuuuuuuuujuuuuujuuuuuujuujujuuuuuuujuuuuuujuujuuuujjuuuuuuujuuuuuujuuuuujjujuuuuuuuuuuujuujjuuujuuuuuuuuuuuuujujuuuujujuuujuuuuuuujuuuuuuujujuuujuuuuuuuuuuujuuuujuujjjuuujuuuuujuuuuuujujujujujuuuuuuuuuujuuujuujuuuuujuuuujjuuuuuujujjuuujujuuuujuuuuuuujuuuuuuuuuujuuujuuuuuuujuuujujuuuuuuuuuuuuuuuuujuuujjuuuuuuuuujuuujuuuuuuuuuujjjuuuuuuuuuuujjuujuujuuuuuujuuuuuujuuuuuuuuuuujujuuujuuujujjuuuuuuujuuuuuuuuuujuuujuuuuujuuuuuuuuuujuuujjjujuuujuujujuuuuuuuujuuuujuuuuujuujujuuujuujuuuuuuuuujuujuuuuuuuujuuuuuuuuuuuuuuujuuujjuuuuuuuuuuuuujuuuuuuuuuujuuuuujuuuuuuuuuuuuuujuujuujjuujujuujuuuuuujuuuuuujuuuuuuuuuuuuuuuujuujuuuuuuuuujuujuuuuujuuuujjuujuuujuuuuuuuuuuujuuuujjuuuuuujuuujuuujjujuuuuuuuuuuuuuuujuuuuujuuuuujuuujjjuuujuuuuuuuuuujuujjujujuujuujuuuujuuuuuuuuuujjuuuuuuujuuuujuuuujuuuuuuuuuujuujujujuuuuuuujuuuuuuuuuuuujuuujjuuuuujuuuuuuuuuuuuuuuuuuuujuujuuuuuuuuuuuujuuuujuuuujjjuujuuuuuuujjuuujuuuuuuuuuuuuuuuujujuuuuujujujuuuuuuuuujuuuuuuuuuuuuuuuuuuuuujuuuuuuuuuuuuujujjujuuuuuuuuuujuuujujuuuuuuuuuujjuujuujuuujuuuuujujujujuuuuuuuuuuuuuuuuuuuuuuuujuuuujuuuujjuuuuuuuuuuuuuuuuuuuuuujuuuuuuuuuuuuuuuuuuuuuuuuuuujuuuuujuuuuujuuuuuuuuuuuuuuuujuuuuuujujujuujujjuujuujujuujuuuuuuuuuuuujuuujjjuuuuuuuujjuuuuuuujuuuuuuuuuuuuuuujuuuuuuuuuuuujuuuuuuuuuuuuuuujjuuuuuuuuujjjuuuuuuujuuuuuuujujjuuuuujuujuuujuuuuuuuuuuuujujjjuuuujuuuuujjuuuuuuuujjujuuuuuuuuuuuujjjuuujuujuuuuuuuuuuuuuuujuuuuuuuujujujuujuuuuuujuuujuuuuuuuuuuujuuuuujujuuujuuuuuuuuujuujuuuuuuuuuujuuuuuuuuuujuujuuuuuujuuuuuuuuuuuuuuuujuuuuuujuuuujuuuuuujuuuuujuuuuuuuujujuuujuujjuuuujuuuuuujuuuuujuujjujujuujuuuuuujujuuuuuuujuuujuuujuuuuuuuuuuujuuuuuujujjujuuuuujuuuuujujuujjuuuuuuuujjjuujuuuuuuuuujuuuuuuuuuuuuuuujujuuuujuuuuujuuuuuuuujuuuuuuuuuuuuuuuuuujuuuuuuuuujjujuuuuujuuuuuuuujujuuujuuujjujuuuuuuuuuuuuuuujujuuuuuujuuuuuuuuuuuuujjuuuuuuuuujuuuujuuuuuuuujuuuuujuuuuuuuuuujujuuuuuuuuuuuuuujuuuuujjuuuuuuujuuujuujuuuuuujuuujuuuuuujujuujujuuuuuujujuuuuujuuuuujujujuujjjjuuuuuuuujujuujuuujuuuuuu",
        word2="uuujuujujjjjjjjuujjjjuujjjjjjjjjjjjuujjjjujjjuujujujjjjjjjjjjjjjjjjujujjjjujjjjjjjjjujjjjjjjjjjjjuujjjjjuujujjjjjjjjujjujjjujjjjjjjjjjjjjjjjujjjjjjjjujjjjjjjjjjjjjjjujuuujujujjjujujjuujjjjjjjjjujjjjjjjujjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjujjjjjujjujujjjjjjjuujjjjjjjjjjjjujjjjjjjjjjjjjjjjjujujjjujjjjjjjjujjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjuuujjjjjjjjujujjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjujjjjjjjjjjjjjujjujjjjjjujujjjjjjjjjujjjjjjjjjjjjjjjjjjjjjujjjjjujjjujjjjjjjjjjjjjjjjjjjjujjjjjjjjujjjjjjjjjjjjjjjjjjuujjjjjjjujjjuujjjjjjjjjjjjjjjjjjjujjjujjjjjujjjjjuujjjjjjjjuujjujjjjjjjjjjjjjjjujjujjjjjjjjujujjujjjuujjjjjjjjjjjjjjjujjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjujjjjjjjjjjjjjuujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjuujjjjjujjjjjjjjjujjjjjjujjjjjjjjjjjjjjjjjuujjjjjjjjjjjjjjjjjjjjjujjjjjujujjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjujujjuujjjjjjjjjjjjjjjjjjjujjjjjujujjjjjjujjuujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjuuujjjjjjjuujjjjjjjjjjjjjjujjjjjjjjjujjjjujjjujjjjjjjjjjjjjjjjjujjujjjjjjjjjjjjjjjjujuuujjjujjjjjjjjjjjjujjjujjjjjujjjjjjjjujjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjujjjujujjujjjujujjjjujjjjjjjjjjjuujuujjjjujjjjjjjjjujjjjjjjjujjjjjjjjujjjujjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjuuujjjjjjjjujujujjujjjujjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjujujjjjuujjjujujjjjjujjjjjjjjjjjjjjjujjjjujjjujjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjujjuujujjujjjjjjjjjjjjjjujjjjjjujjjjjjjjjjujjjjuuujjjjjjjjujjuujjjjjjjujjjjjjjujjjjujujjjjjjjjjjjjjjjjjjjjjjjjjjuujjjjjjjjjjjjjujjjjjjjjuujjjujjjjujjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjujjujujjjjjjjjjjjjujjjjjjjjujjjjujjujuujjjjjujjjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjujjjujujjjjjjjjjjjjjjjjujjjjjjujjuujjjjjujjjjjjjujjjjuujjjujjjjjjjjjjjjjjjjujjjjjjjjjjjjujjjjjuuuujjjujjjjjjjjjjjjjjuujuujjjjjjjjjjujujjjjujjujjjjjjujjujjujjjjjjjujujujjujjjjjjjujjjjujjuuujjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjujjjujjjjjjjjjujjjjjjjjujjjjjjjjjjjjjjjujjjjjjujjjjjjjjujjjjjjjujjjjjujjjjjjjujjujjjjjjjjjjjjjujjju"))
