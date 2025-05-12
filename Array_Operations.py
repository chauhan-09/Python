arr = [1,2,3,4,"red",1.025]   

#this is a list
#A list is hetrogeneous , ordered , mutable

print(arr[0])
print(arr[4])
print(arr[-2])
arr.append(5)
print(arr)


def findsum(nums):
    sum = 0
    n = len(nums)
    for i in range(0,n):
      sum += nums[i]    
    return sum


arr2 = [1,2,3,4,5,6,700,79]

print(findsum(arr2))