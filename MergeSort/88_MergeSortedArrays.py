"""
🔹 Problem: Q88 - Merge Sorted Array  
🔗 LeetCode: https://leetcode.com/problems/merge-sorted-array/

🧠 Approach:
- Used two pointers `i` and `j` to traverse `nums1` and `nums2`.
- Compared values and built a new `res` array with merged sorted values.
- Extended with remaining elements of both arrays.
- Overwrote `nums1` in-place with merged result.

⚠️ Status: Accepted ✅

📚 Learning:
- For in-place problems, it's okay to use an intermediate array if allowed.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []
        i = j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        res.extend(nums1[i:m])
        res.extend(nums2[j:n])

        for idx in range(len(res)):
            nums1[idx] = res[idx]
