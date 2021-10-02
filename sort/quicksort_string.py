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

names = [
         'Alanna Penton',
         'Epifania Nason',
         'Anisha Brayton',
         'Corina Rossignol',
         'Edward Setser',
         'Evon Ulmer',
         'Helaine Beeson',
         'Tenesha Dedeaux',
         'Marilu Painter',
         'Vena Gibbs',
         'Dania Duffel',
         'Florida Brust',
         'Marchelle Haberkorn',
         'Sylvie Lish',
         'Isaias Ables',
         'Geraldine Pavlick',
         'Beryl Columbia',
         'Colette Hiebert',
         'Shawnda Canada',
         'Gonzalo Manning',
         'Tamar Piersall',
         'Serita Mckernan',
         'Leonardo Whitelaw',
         'Brigid Caton',
         'Landon Levinson',
         'Chieko Kinnear',
         'Chrissy Hayne',
         'Eloy Maple',
         'Sade Norman',
         'Kamilah Rex',
         'Laticia Eckel',
         'Delia Vegas',
         'Pia Adamczyk',
         'Dorthey Truby',
         'Arlean Mcfadin',
         'Leatha Vieira',
         'Estrella Tremper',
         'Libby Chivers',
         'Yolande Burritt',
         'Lavon Montealegre',
         'Lynsey Barley',
         'Marisol Neher',
         'Rudolf Grossi',
         'Marketta Howey',
         'Assunta Wessels',
         'Laurene Digennaro',
         'Janell Lizotte',
         'Malik Slovinsky',
         'Shawnta Hertel',
         'Pamula Gracia']

result = quicksort(names)
print(result)