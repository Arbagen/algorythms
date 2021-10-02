import random

numbers = [1,5,2,4,5,7,9,2,34,62]

def is_sorted(list):
  for index in range(len(list) - 1):
    if list[index] > list[index + 1]:
      return False
  return True

def bogo_sort(list):
  while not is_sorted(list):
    random.shuffle(list)
  return list

print(bogo_sort(numbers))