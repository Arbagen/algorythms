import random
def selection_sort(list):
  sorted = []
  for index in range(0, len(list)):
    new_index = index_of_min(list)
    sorted.append(list.pop(new_index))
  return sorted

def index_of_min(list):
  minimum_index = 0
  for index in range(1, len(list)):
    if list[index] < list[minimum_index]:
      minimum_index = index
  return minimum_index

numbers = list(range(1, 10000))
random.shuffle(numbers)
selection_sort(numbers)
# print(selection_sort(numbers))