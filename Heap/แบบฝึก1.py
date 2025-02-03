import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, value):
        heapq.heappush(self.heap, -value)  # เก็บค่าติดลบเพื่อให้ heapq ทำงานเป็น Max Heap
    def pop(self):
        return -heapq.heappop(self.heap) 
    def get_heap(self):
        return sorted([-val for val in self.heap], reverse=True)  # คืนค่าตามลำดับ Max Heap
max_heap = MaxHeap()
values = [2, 3, 4, 5, 6, 7, 8, 9]
for v in values:
    max_heap.push(v)
print("Max Heap:", max_heap.get_heap())
