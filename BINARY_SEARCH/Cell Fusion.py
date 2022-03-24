import heapq
class Solution:
    def solve(self, cells):
        pq = [-cell for cell in cells]
        heapq.heapify(pq)
        while len(pq) > 1:
            a, b = heapq.heappop(pq), heapq.heappop(pq)
            if a != b:
                heapq.heappush(pq, (-a - b) // 3 * -1)
        return -1 if not pq else -pq[0]

cells = [1,3,3,4]
s=Solution()
print(s.solve(cells))