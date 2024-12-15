class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        indexes = list(range(n))

        self.counting_inversions(nums, indexes, 0, n-1, res)
        return res

    def counting_inversions(self, nums, indexes, s, e, res):
        if s >= e: return 0
        
        mid = (s + e) // 2
        count = 0

        cleft = self.counting_inversions(nums, indexes, s, mid, res)
        cright = self.counting_inversions(nums, indexes, mid + 1, e, res)

        cmerge = self.merge_and_count(nums, indexes, s, mid, e, res)

        return cleft + cright + cmerge

    def merge_and_count(self, nums, indexes, s, m, e, res):
        a, b = s, m + 1
        merged = []
        count = 0
        
        while a <= m and b <= e:
            if nums[indexes[a]] <= nums[indexes[b]]:
                merged.append(indexes[a])
                res[indexes[a]] += count
                a += 1
            else:
                merged.append(indexes[b])
                count += 1
                b += 1
        
        while a <= m:
            merged.append(indexes[a])
            res[indexes[a]] += count
            a += 1
        
        while b <= e:
            merged.append(indexes[b])
            b += 1
        
        for i in range(len(merged)): indexes[s + i] = merged[i]
        
        return count