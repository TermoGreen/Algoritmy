"""O(n)"""
class solution:
    def getMaximumGenerated(self, x):
        num = [0] * (x + 2)
        num[1] = 1
        for i in range(2, x + 1):
            num[i] = num[i // 2] + num[(i // 2) + 1] * (i % 2)       # условия в действии

        return max(num[:x + 1])        # вернул из функции num