import heapq
class ProductRanking:
    def __init__(self, k):
        self.k = k
        self.products = []  # Min Heap เก็บ k สินค้าขายดีที่สุด
    
    def update_sales(self, product_id, sales):
        # ถ้ายังมีช่องว่างใน heap หรือสินค้าที่ขายมากกว่าค่าต่ำสุดใน heap
        if len(self.products) < self.k:
            heapq.heappush(self.products, (sales, product_id))
        else:
            if sales > self.products[0][0]:  
                heapq.heapreplace(self.products, (sales, product_id))
    
    def get_top_k(self):
        
        return sorted(self.products, reverse=True, key=lambda x: x[0])

    def __repr__(self):
        return f"ProductRanking(k={self.k}, top_k={self.get_top_k()})"
ranking = ProductRanking(3)  # เก็บ 3 อันดับสินค้าขายดี
ranking.update_sales("สินค้า A", 100)
ranking.update_sales("สินค้า B", 150)
ranking.update_sales("สินค้า C", 80)
ranking.update_sales("สินค้า D", 200)
print(ranking.get_top_k())