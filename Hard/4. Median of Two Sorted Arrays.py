def median(arr):
    if len(arr) % 2:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2.0

class Solution(object):
    # could defeinitely be improved, i think my edge case handling is terrible
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        odd =(len(nums1)+ len(nums2)) % 2
        while nums1 and nums2:
            l = len(nums1) + len(nums2)
            if l == 2 and not odd:
                new = nums1 + nums2
                return sum(new) / 2.0
            if l == 1: 
                    new = nums1 + nums2
                    return new[0]

            if len(nums2) >= 2:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else: 
                    nums2.pop(0)

                if not nums2: break

                if nums1 and nums1[-1] > nums2[-1]:
                    nums1.pop(-1)
                else:
                    nums2.pop(-1)
                odd =(len(nums1) + len(nums2)) % 2

            else: break

        new = nums1 + nums2
        print("this is new" + str(new))
        new.sort()
        return median(new)

                
        

            
            
        
