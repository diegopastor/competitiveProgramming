import heapq

def lastStoneWeight(stones):
    heap = [stone*-1 for stone in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)
        if s1 != s2:
            heapq.heappush(heap, s1 - s2)
    if len(heap) == 0:
        return 0
    else:
        return -1 * heap[0]

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1,1,1,1,1,1]))
