from typing import List


# 情景模拟
# O(N×K)
# O(K)
# 超出时间限制


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # 每个服务器的处理请求数（用于生成答案）
        finish_num = [0] * k

        # 每个服务器的结束时间
        finish_time = [0] * k

        # 情景模拟
        for i in range(len(arrival)):
            now = arrival[i]

            # 计算当前请求优先的服务器
            idx = i % k

            # 分配服务器
            for j in range(k):
                if finish_time[idx] <= now:
                    finish_time[idx] = now + load[i]
                    finish_num[idx] += 1
                    break
            else:
                # 请求被忽略
                pass

        # 计算最终结果
        max_idx, max_val = [], -1
        for i in range(k):
            if finish_num[i] > max_val:
                max_idx = [i]
                max_val = finish_num[i]
            elif finish_num[i] == max_val:
                max_idx.append(i)

        return max_idx


if __name__ == "__main__":
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))  # [1]
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]))  # [0]
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11]))  # [0,1,2]
    print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4, 8, 9, 10], load=[5, 2, 10, 3, 1, 2, 2]))  # [1]
    print(Solution().busiestServers(k=1, arrival=[1], load=[1]))  # [0]
