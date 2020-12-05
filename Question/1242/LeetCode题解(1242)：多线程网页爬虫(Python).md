# LeetCode题解(1242)：多线程网页爬虫(Python)

题目：[原题链接](https://leetcode-cn.com/problems/web-crawler-multithreaded/)（中等）

标签：多线程、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 344ms (36.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import collections
import queue
import threading
from urllib.parse import urlsplit

class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = urlsplit(startUrl).netloc
        request_queue = queue.Queue()
        result_queue = queue.Queue()
        request_queue.put(startUrl)

        # 启动线程
        for _ in range(5):
            thread = threading.Thread(target=self._run, args=(domain, htmlParser, request_queue, result_queue))
            thread.daemon = True
            thread.start()

        running = 1
        visited = {startUrl}

        while running:
            for url in result_queue.get():
                if url not in visited:
                    visited.add(url)
                    request_queue.put(url)
                    running += 1
            running -= 1

        return list(visited)

    def _run(self, domain, htmlParser, request_queue, result_queue):
        while True:
            now_url = request_queue.get()
            next_url_lst = []
            for next_url in htmlParser.getUrls(now_url):
                if domain == urlsplit(next_url).netloc:
                    next_url_lst.append(next_url)
            result_queue.put(next_url_lst)
```