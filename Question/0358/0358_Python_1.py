import collections
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        size = len(s)

        # 生成字符数量堆
        count = collections.Counter(s)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)

        # 生成字符等待队列
        queue = collections.deque()

        ans = []
        for i in range(size):
            # 取出等待队列队首的字符
            if i >= k and queue:
                element = queue.popleft()
                if element != (None, None):
                    heapq.heappush(heap, element)

            # 从堆中提取频率最高的字符
            if not heap:
                return ""
            count, ch = heapq.heappop(heap)

            # 将字符添加到结果
            ans.append(ch)

            # 将字符添加到等待队列
            if count + 1 < 0:
                queue.append((count + 1, ch))
            else:
                queue.append((None, None))  # 如果字符已经用完则添加空位

        return "".join(ans)


if __name__ == "__main__":
    # "abcabc"
    print(Solution().rearrangeString(s="aabbcc", k=3))

    # ""
    print(Solution().rearrangeString(s="aaabc", k=3))

    # "abacabcd"
    print(Solution().rearrangeString(s="aaadbbcc", k=2))
