# LeetCode题解(0730)：字符串的不同的非空回文子序列数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-different-palindromic-subsequences/)（困难）

标签：字符串、动态规划、动态规划-状态表格

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 4436ms (16.13%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 528ms (100.00%) |
| Ans 3 (Python) |            |            |                 |

解法一（动态规划）：

```python
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(S)

        dp = [[[0] * N for _ in range(N)] for _ in range(4)]  # 状态表格

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                for k in range(4):
                    ch = ["a", "b", "c", "d"][k]
                    if i == j:
                        if S[i] == ch:
                            # 转移方程：DP[x][i][j] = 1（i=j且S[i]=ch）->即只有一个字符的字符串，包含本身一个以目标字符开头的回文串
                            dp[k][i][j] = 1
                        # 转移方程：DP[x][i][j] = 0（i=j且S[i]!=ch）->即只有一个字符的字符串，没有以目标字符开头的回文串（因默认为0不再设置）
                    else:  # 此时：i<j
                        if S[i] != ch:
                            # 转移方程：DP[x][i][j] = DP[k][i+1][j]（i<j且S[i]!=ch）->因为不是以目标字符开头的，所以以目标字符开头的回文串数量与跳过开头字符的情况相同
                            dp[k][i][j] = dp[k][i + 1][j]
                        elif S[j] != ch:
                            # 转移方程：DP[x][i][j] = DP[k][i+1][j]（i<j且S[j]!=ch）->因为新增字符不是目标字符，所以以目标字符开头的回文串数量与跳过最后一个字符的情况相同
                            dp[k][i][j] = dp[k][i][j - 1]
                        else:  # 此时：i<j且S[i]==S[j]==ch
                            if j == i + 1:
                                # 转移方程：DP[x][i][j] = 2（j=i+1且S[i]=S[j]=ch）->即有两个相同字符的字符串（aa），包含两个非空回文串（a）和（aa）
                                dp[k][i][j] = 2
                            else:  # 此时：i<j+1且S[i]==S[j]==ch
                                # 转移方程：DP[x][i][j] = 2+DP[0][i+1][j-1]+DP[1][i+1][j-1]+DP[2][i+1][j-1]+DP[3][i+1][j-1]
                                # 新增首尾两个字符自行组成的两种情况；以及内部所有回文串增加了嵌套于两个目标字符之间的新回文串
                                dp[k][i][j] = 2  # 通过首尾两个字符（aa）自行组成的回文串（a）和（aa）
                                for m in range(4):  # 累加首尾两个字符内部包含的回文串数量->内部所有的回文串均增加了嵌套于两个目标字符之间的新回文串
                                    dp[k][i][j] += dp[m][i + 1][j - 1]
                                    dp[k][i][j] %= MOD

        ans = 0
        for k in range(4):  # 遍历以每个字符开头的情况
            ans += dp[k][0][N - 1]  # 以目标字符开头的，从头到尾的完整字符串
            ans %= MOD
        return ans
```

解法二（数学）：

![image-20200818074353343](LeetCode题解(0730)：截图1.png)

```python
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        N = len(S)
        MOD = 1000000007

        # nxt记录在当前字符之后，截止当前的j之前，一共有多少个回文串；例如：bccb中j=2时，当前nxt[0]=2，因为在第1个b之后有2个回文串c和cc
        nxt = [0] * N
        # use用于去重，记录当前字符之后的回文串中，已被计入到ans中的回文串有多少个；例如：bccb中j=3时，use[0]=3，第1个b之后有3个回文串c、cc和b，但都已经被最后一个b收获掉了
        use = [0] * N
        # nxt[i]-use[i] : 当前可以收获的数量
        # “收获”可理解为：从i+1开始，还有多少个回文串没有被前后两个S[i]嵌套；也就是当一个新的S[j]=S[i]后，可以通过前后嵌套的S[i]和S[j]来新增的回文串数量

        ans = 0
        for j in range(N):
            # 新字符直接带来的仅包含当前字符的回文串，例如b->b；bc->c；bcc->cc；bccb->bb
            x = 1

            for i in range(j - 1, -1, -1):
                # 字符S[i]等于新增字符S[j]，则收获S[i]字符之后未收获的回文串
                if S[i] == S[j]:
                    # x : 此时的x是当前字符S[i]之后因为当前新增字符S[j]而新增的回文串数量

                    # now_nxt : 当前字符S[i]后可收获的回文串数量
                    now_nxt = nxt[i]

                    # now_use : 当前字符S[i]后已收获的回文串数量
                    now_use = use[i]

                    # 将新增的回文串数量添加到S[i]中，这些回文串是因为新增字符才新增的，所以并不能在这次被直接收获，需要等待下一个相同的字符
                    nxt[i] += x

                    # 计算当前可以收获的新增回文串数量：可收获的数量-已收获的数量
                    # 对于相同的字符来说，靠前的字符中记录的回文串数量，一定已经包含靠后的字符中记录的回文串数量（不使用+=的原因）
                    x = now_nxt - now_use + 1

                    # 将这一次收获的回文串回文串数量累计到已收获的回文串数量之中
                    use[i] = now_nxt + 1

                # 字符S[i]不等于新增字符S[j]，新增字符不能收获新的回文串，但是对于i来说，它后面又新增了x个回文串，以备之后收获
                else:
                    nxt[i] += x

            # 记录当前字符新增的回文串数
            ans += x
        return ans % MOD
```