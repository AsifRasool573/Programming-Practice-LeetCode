# 34. Find First and Last Position of Element in Sorted Array

Problem Statement:

#Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



# 1. *** first logic

nums = [5,7,7,8,8,8,10,10]
target = 10
result = []


for i in range(len(nums)):
  if(nums[i] == target):
    result.append(i)

if(len(result)==0):
  print([-1,-1])
else:
  print(result)

======================================================================================================
======================================================================================================


# 2. *** Second Logic

nums = [1]
target = 1

result = []

if target not in nums:
  print([-1,-1])

if (len(nums) == 1 and target in nums):
  print([0,0])


for i in range(len(nums)):
    if(nums[i] == target):
      result.append(i)

print(result)


======================================================================================================
======================================================================================================


# 2. *** Third Logic (Working)


# Final Code
nums = [5,7,8,8,9,10]
target = 9

if target not in nums:
  print ([-1, -1])

first_idx = nums.index(target)
hold = first_idx

for i in range(first_idx + 1 , len(nums)):

  if nums[i]!=target:
    break
    
  hold = i

print([first_idx, hold])