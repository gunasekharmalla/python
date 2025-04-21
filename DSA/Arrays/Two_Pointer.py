    ## Move All Negative Numbers to One Side
Input: [-1, 2, -3, 4, -5, 6]
Output: [-1, -3, -5, 4, 2, 6]
#program:
  nums=[-1,2,-3,4,-5,6]
  l=0
  r=0
  for r in range(len(nums)):
      if nums[r]<0:
          nums[r],nums[l]=nums[l],nums[r]
          l+=1
  print(nums)
