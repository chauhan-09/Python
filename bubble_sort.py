arr = [10,4,20,5,7,1,2,8,3,4]
n = len(arr)

def bubble_sort(arr):
  for i in range(n):
    flag = True
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
          arr[j] , arr[j+1] = arr[j+1] , arr[j]
          flag = False
    if flag:
      break


bubble_sort(arr)
print(arr)


cars = ["bmw","toyota","nano"] #tuple unpacking
car1 , car2 , car3 = cars
print(car1)
print(car2)
print(car3)