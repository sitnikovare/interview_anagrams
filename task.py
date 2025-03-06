## Считаем, что при пустом входном массиве должен быть возвращен пустой массив
## Одно слово является анаграммой самому себе
## Объекты, не являющиеся строкой, игнорируются

# функция получения анаграммы
def getAnagram(arr):
  #  если массив пуст, нечего возвращать
  if (len(arr) < 2): return arr

  # хранит результат
  res = [];

  # цикл по всему массиву
  for i in range(0, len(arr)):

    # проверка, было ли данное слово уже добавлено
    # так как добавляется сразу и слово, и его анаграмма
    # а так же на то, что объект является строкой
    if (not isinstance(arr[i], str) or (arr[i] in res)): continue

    # приведение к нижнему регистру и разбивка на буквы
    letters = sorted(list(arr[i].lower()))

    # поиск анаграмм
    for j in range(0, len(arr)):
      # пропуск текущего слова
      if (i == j or not isinstance(arr[j], str)):
        continue
      
      # приведение к нижнему регистру и разбивка на буквы для проверяемого слова
      lettersNew = sorted(list(arr[j].lower()))
      if (letters == lettersNew):
        if arr[i] not in res: res.append(arr[i])
        if arr[j] not in res: res.append(arr[j])
      
  # возвращение результата с приведением к массиву
  return res

array = [12, "Сон", 21, "Нос"]
print(getAnagram(array))