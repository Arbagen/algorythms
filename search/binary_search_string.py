def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None

names = ['Alanna Penton', 'Anisha Brayton', 'Arlean Mcfadin', 'Assunta Wessels', 'Beryl Columbia', 'Brigid Caton', 'Chieko Kinnear', 'Chrissy Hayne', 'Colette Hiebert', 'Corina Rossignol', 'Dania Duffel', 'Delia Vegas', 'Dorthey Truby', 'Edward Setser', 'Eloy Maple', 'Epifania Nason', 'Estrella Tremper', 'Evon Ulmer', 'Florida Brust', 'Geraldine Pavlick', 'Gonzalo Manning', 'Helaine Beeson', 'Isaias Ables', 'Janell Lizotte', 'Kamilah Rex', 'Landon Levinson', 'Laticia Eckel', 'Laurene Digennaro', 'Lavon Montealegre', 'Leatha Vieira', 'Leonardo Whitelaw', 'Libby Chivers', 'Lynsey Barley', 'Malik Slovinsky', 'Marchelle Haberkorn', 'Marilu Painter', 'Marisol Neher', 'Marketta Howey', 'Pamula Gracia', 'Pia Adamczyk', 'Rudolf Grossi', 'Sade Norman', 'Serita Mckernan', 'Shawnda Canada', 'Shawnta Hertel', 'Sylvie Lish', 'Tamar Piersall', 'Tenesha Dedeaux', 'Vena Gibbs', 'Yolande Burritt']

print(len(names))
search = ['Marisol Neher', 'Chieko Kinnear', 'Dania Duffel', 'Edward Setser','Yolande Burritt', 'Alanna Penton']

for name in search:
    result = binary_search(names, name)
    print(result)
