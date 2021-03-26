from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0

        count_from = [0] * n
        count_to = [0] * n
        now_requests = []

        # 数量统计
        for request in requests:
            if request[0] == request[1]:
                ans += 1
            else:
                now_requests.append((request[0], request[1]))
                count_from[request[0]] += 1
                count_to[request[1]] += 1

        # 不断筛选
        while True:
            # 判断是否剩余请求均可满足
            for i in range(n):
                if count_from[i] != count_to[i]:
                    break
            else:
                return ans + len(now_requests)

            # 过滤绝对不可能完成的请求
            new_requests = []
            for request in now_requests:
                if count_from[request[1]] == 0:
                    count_to[request[1]] -= 1
                    count_from[request[0]] -= 1
                else:
                    new_requests.append(request)

            # 处理过滤了不可能完成的请求的情况
            if len(new_requests) != len(now_requests):
                now_requests = new_requests
                continue

            else:
                # 递归处理可选择的不可能完成的请求
                for i in range(n):
                    if count_from[i] < count_to[i]:
                        maybe_lst = []
                        for request in now_requests:
                            if request[1] == i:
                                maybe_lst.append(request)

                        part_max = 0
                        for maybe in maybe_lst:
                            now_requests.remove(maybe)
                            part_max = max(part_max, self.maximumRequests(n, now_requests))
                            now_requests.append(maybe)

                        return ans + part_max


if __name__ == "__main__":
    print(Solution().maximumRequests(n=5, requests=[[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))  # 5
    print(Solution().maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]))  # 3
    print(Solution().maximumRequests(n=4, requests=[[0, 3], [3, 1], [1, 2], [2, 0]]))  # 4
