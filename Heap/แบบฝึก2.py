import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, value):
        heapq.heappush(self.heap, -value)  
    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None   
    def get_heap(self):
        return sorted([-val for val in self.heap], reverse=True)  # คืนค่าตามลำดับ Max Heap
max_heap = MaxHeap()
values = [2, 3, 4, 5, 6, 7, 2, 9]
for v in values:
    max_heap.push(v)
print("Initial Max Heap:", max_heap.get_heap())
for i in range(1, 4):
    removed = max_heap.pop()
    print(f"After removing {removed}: {max_heap.get_heap()}")
