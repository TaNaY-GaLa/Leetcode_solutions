class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        x = 0
        while x < len(nums1):
            ans = -1
            i = 0
            while i < len(nums2):
                if nums2[i] == nums1[x]:
                    j = i + 1
                    while j < len(nums2):
                        if nums2[j] > nums1[x]:
                            ans = nums2[j]
                            break
                        j += 1
                    break
                i += 1
            res.append(ans)
            x += 1
        return res