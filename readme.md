# Файл task.py

Функция getAnagram(arr) производит поиск анаграмм в массиве.
Вход: массив объектов.
Выход: массив, содержащий только слова-анаграммы или пустой массив.

Условия:

- При пустом входном массиве должен быть возвращен пустой массив.
- Одно слово является анаграммой самому себе.
- Объекты, не являющиеся строкой, должны быть проигнорированы.

# Файл tests.py

Содержит юнит-тесты для функции:

- test_Has1Anagram_oneLetterCase - пример с интервью
- test_Has2Anagram_twoLetterCases - две пары анаграмм, разные регистры букв
- test_Has1Anagram_ingoreDigits - одна анаграмма, числа игнорируются
- test_Has2Anagram_ingoreSpecials - две анаграммы, объекты не строчного типа инорируются
- test_EmptyArray - пустой массив
- test_NoAnagram1 - массив не содержи слов-анаграмм
- test_NoAnagram2 - в слове cердцевинA заглавная А на латинице
- test_NoAnagram3 - числа игнорируются
- test_СheckСaseOfLetters - проверка, что функция возвращает слова в изначальном виде

# Github Actions

Настроены на пулл-реквесты и на пуши в мастер, результат после предыдущего пуша:
============================= test session starts ==============================
platform linux -- Python 3.10.16, pytest-8.3.5, pluggy-1.5.0 -- /opt/hostedtoolcache/Python/3.10.16/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/interview_anagrams/interview_anagrams
collecting ... collected 9 items

tests.py::test*Has1Anagram_oneLetterCase PASSED [ 11%]
tests.py::test_Has2Anagram_twoLetterCases PASSED [ 22%]
tests.py::test_Has1Anagram_ingoreDigits PASSED [ 33%]
tests.py::test_Has2Anagram_ingoreSpecials PASSED [ 44%]
tests.py::test_EmptyArray PASSED [ 55%]
tests.py::test_NoAnagram1 PASSED [ 66%]
tests.py::test_NoAnagram2 PASSED [ 77%]
tests.py::test_NoAnagram3 PASSED [ 88%]
tests.py::test*СheckСaseOfLetters PASSED [100%]

============================== 9 passed in 0.02s ===============================
