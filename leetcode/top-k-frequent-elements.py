import heapq

def topK(nums, k):
    freqs = {}
    for n in nums:
        if n in freqs:
            freqs[n] += 1
        else:
            freqs[n] = 1

    heap = []

    for n, times in freqs.items():
        heapq.heappush(heap, (times, n))
        if len(heap) > k:
            heapq.heappop(heap)
    
    ans = []
    while heap:
        ans.append(heapq.heappop(heap)[1])

    return ans


print(topK([1,1,1,2,2,3], 2))
print(topK([1], 1))
