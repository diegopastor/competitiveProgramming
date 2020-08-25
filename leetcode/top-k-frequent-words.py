import heapq

"""
Complexity of O(n * log k)
"""

class Occurences:
    def __init__(self, word, n):
        self.word = word
        self.n = n

    def __lt__(self, other):
        if self.n == other.n:
            return self.word > other.word
        else:
            return self.n < other.n

def topKFrequent(words, k):
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    heap = []
    for word, count in occurences.items():
        t = Occurences(word, count)
        heapq.heappush(heap, t)
        # Priority Queues have a worst time complexity of
        # O(log n) when inserting, in order to keep the complexity
        # under O(log k) we remove the smallest element if heap 
        # gets bigger than k
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    while len(heap):
        result.append(heapq.heappop(heap).word)
    return result[::-1]

print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
