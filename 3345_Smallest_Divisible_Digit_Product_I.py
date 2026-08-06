class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n

        def pro(current):
            product = 1
            while current > 0:
                digit = current % 10
                product *= digit 
                current = current // 10
            return product 
            
        while True:
            product = pro(current)
            if product % t == 0:
                return current 
            current += 1