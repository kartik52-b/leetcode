class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        bit_size = 2 * n + 2
        bit = [0] * bit_size
        
        def update(i, delta):
            while i < bit_size:
                bit[i] += delta
                i += i & (-i)
        
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
            
        offset = n + 1
        current_sum = 0
        ans = 0
        
        update(offset, 1)
        
        for num in nums:
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
            
            ans += query(current_sum + offset - 1)
            update(current_sum + offset, 1)
            
        return ans