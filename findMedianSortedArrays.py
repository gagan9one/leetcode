# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 23:06:40 2019
Leetcode Problem : https://leetcode.com/problems/median-of-two-sorted-arrays
@author: gagan
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr1=[]
        arr2=[]
        if(len(nums1)<=len(nums2)):
            arr1=nums1
            arr2=nums2
        else:
            arr1=nums2
            arr2=nums1
        flag = False
        lenX = len(arr1)
        lenY = len(arr2)
        start = 0
        end = lenX
        while(start<=end):
            partX = (start + end)//2
            partY = (lenX + lenY + 1)//2 - partX
            partXLeft = (float('-inf') if partX==0 else arr1[partX-1])
            partYRight = (float('inf') if partY==lenY else arr2[partY])
            partYLeft = (float('-inf') if partY==0 else arr2[partY-1])
            partXRight = (float('inf') if partX==lenX else arr1[partX])
            if(partXLeft>partYRight):
                end = partX-1
            elif(partYLeft>partXRight):

                start = partX + 1
            else:
                flag = True
                
                if((lenX+lenY)%2==0):
                    return((max(partXLeft,partYLeft)+ min(partXRight,partYRight))/2)
                else:

                    return max(partXLeft,partYLeft)
obj = Solution()
print(obj.findMedianSortedArrays([1,3],[2]))