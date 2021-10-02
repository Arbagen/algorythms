import random

def quicksort(list):
  if len(list) <= 1:
    return list
  less_than_pivot = []
  greater_than_pivot = []
  pivot = list[0]
  for value in list[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

numbers = list(range(1, 1000000))
random.shuffle(numbers)
numbers.insert(0, 1)
result = quicksort(numbers)
# print(result)