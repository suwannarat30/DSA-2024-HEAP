class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, value):
        self.heap.append(value)  # เพิ่มค่าเข้าไปใน heap
        self._heapify_up(len(self.heap) - 1)   
    def pop(self):
        if not self.heap:
            return None
        # สลับค่ารากกับค่าตัวสุดท้าย
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._heapify_down(0)  # เรียงลำดับหลังลบค่า
        return max_value
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def get_heap(self):
        return self.heap  # แสดงผลลัพธ์ของ Max Heap ตามลำดับ

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent]:
                self._swap(idx, parent)
                idx = parent
            else:
                break
    
    def _heapify_down(self, idx):
        size = len(self.heap)
        while 2 * idx + 1 < size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != idx:
                self._swap(idx, largest)
                idx = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2):  
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True
elements = [2, 3, 4, 5, 6, 7, 8, 9]
max_heap = MaxHeap()
for element in elements:
    max_heap.push(element)
print("Max Heap:", max_heap.get_heap())
for i in range(3):
    removed = max_heap.pop()
    print(f"หลังจากลบ {removed}:", max_heap.get_heap())
print("เป็น Max Heap หรือไม่:", is_max_heap(max_heap.get_heap()))