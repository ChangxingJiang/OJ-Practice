# LeetCode题解(1681)：最小不兼容性(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-incompatibility/)（困难）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 44ms (99.08%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.size = 0
        self.k = 0
        self.ans = 256

    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # 处理无法分配的情况
        if collections.Counter(nums).most_common(1)[0][1] > k:
            return -1

        nums.sort()

        # 处理k为1的情况
        if k == 1:
            return nums[-1] - nums[0]

        # print("初始数组:", nums)

        # 计算每个子集的元素数
        self.k = k
        self.size = len(nums) // k

        # 生成初始情况
        res = []
        for i in range(0, len(nums), self.size):
            res.append(nums[i:i + self.size])

        self.count1(copy.deepcopy(res))

        return self.ans

    def count1(self, res):
        """将数组替换为无重复的情况（不一定是最优解）"""
        # print("初始数组:", res)

        has_same = False

        for i1 in range(self.k):
            sames = self.get_same(res[i1])
            for j1 in sames:
                has_same = True
                n1 = res[i1][j1]

                # 定义备选值
                ii1, jj1 = -1, -1
                ii2, jj2 = -1, -1

                # 向左寻找可替换的值
                i2 = i1 - 1
                while ii1 == -1 and i2 >= 0:
                    if n1 not in res[i2]:
                        for j2 in range(self.size - 1, -1, -1):
                            n2 = res[i2][j2]
                            if n2 not in res[i1]:
                                ii1, jj1 = i2, j2  # 填写备选情况
                                break
                    i2 -= 1

                # 向右寻找可替换的值
                i2 = i1 + 1
                while ii2 == -1 and i2 < self.k:
                    if n1 not in res[i2]:
                        for j2 in range(self.size):
                            n2 = res[i2][j2]
                            if n2 not in res[i1]:
                                ii2, jj2 = i2, j2  # 填写备选情况
                                break
                    i2 += 1

                # print(res, i1, "备选方案:", (ii1, jj1), (ii2, jj2))

                if ii1 != -1 and ii2 != -1:
                    res1 = copy.deepcopy(res)
                    res1[i1][j1], res1[ii1][jj1] = res1[ii1][jj1], res1[i1][j1]
                    res1[i1].sort()
                    res1[ii1].sort()
                    self.count1(res1)

                    res2 = copy.deepcopy(res)
                    res2[i1][j1], res2[ii2][jj2] = res2[ii2][jj2], res2[i1][j1],
                    res2[i1].sort()
                    res2[ii2].sort()
                    self.count1(res2)
                    return
                elif ii2 != -1:
                    res[i1][j1], res[ii2][jj2] = res[ii2][jj2], res[i1][j1]
                    res[i1].sort()
                    res[ii2].sort()
                elif ii1 != -1:
                    res[i1][j1], res[ii1][jj1] = res[ii1][jj1], res[i1][j1]
                    res[i1].sort()
                    res[ii1].sort()

        if not has_same:
            self.count2(copy.deepcopy(res))
        else:
            self.count1(copy.deepcopy(res))

    def count2(self, res):
        """将无重复的数组替换为最优解"""

        # print("符合数组:", res)

        for i1 in range(self.k):
            for j1 in range(self.size):
                n1 = res[i1][j1]

                # 向右寻找可交换的值
                i2 = i1 + 1
                while i2 < self.k:
                    if n1 not in res[i2]:
                        j2 = 0
                        n2 = res[i2][j2]
                        if n2 not in res[i1]:
                            # 条件允许交换，考虑交换是否值得
                            min1_old, max1_old = res[i1][0], res[i1][-1]
                            min2_old, max2_old = res[i2][0], res[i2][-1]

                            temp = copy.copy(res[i1])
                            temp._remove(n1)
                            temp.append(n2)
                            temp.sort()
                            min1_new, max1_new = temp[0], temp[-1]

                            temp = copy.copy(res[i2])
                            temp._remove(n2)
                            temp.append(n1)
                            temp.sort()
                            min2_new, max2_new = temp[0], temp[-1]

                            change1 = (max1_new - min1_new) - (max1_old - min1_old)
                            change2 = (max2_new - min2_new) - (max2_old - min2_old)

                            if change1 + change2 < 0:
                                # print(res, (i1, j1), "<-替换->", (i2, j2))

                                res[i1][j1], res[i2][j2] = res[i2][j2], res[i1][j1]
                                res[i1].sort()
                                res[i2].sort()

                                return self.count2(res)

                    i2 += 1

        # 没有更换则计算最优结果
        else:
            # print("最终数组:", res)
            ans = 0
            for i in range(self.k):
                ans += res[i][-1] - res[i][0]
            self.ans = min(self.ans, ans)

    @staticmethod
    def get_same(lst):
        sets = set()
        res = []
        for i in range(len(lst)):
            if lst[i] not in sets:
                sets.add(lst[i])
            else:
                res.append(i)
        return res
```

