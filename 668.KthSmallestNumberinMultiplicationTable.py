#Hard (MOM)

class Solution(object):
    def findKthNumber(self, m, n, k):

        def count_less_equal(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        def median_of_medians(arr):
            if len(arr) <= 5:
                return sorted(arr)[len(arr) // 2]
            
            sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
            medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
            return median_of_medians(medians)
        
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

# Testes
solution = Solution()

m1 = 3
n1 = 3
k1 = 5
print(solution.findKthNumber(m1, n1, k1))

m2 = 2
n2 = 3
k2 = 6
print(solution.findKthNumber(m2, n2, k2))