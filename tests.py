import sys
sys.path.insert(0, '/tasks')
from task import getAnagram

def test_Has1Anagram_oneLetterCase():
    array = ["кот", "сон", "нос", "творог", "школа", "сокол", "носок"]
    ER = ["сон", "нос"]
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_Has2Anagram_twoLetterCases():
    array = ["Сон", "НОС", "носок", "древЕсница", "горовт", "Сердцевина"]
    ER = ["Сон", "НОС", "древЕсница", "Сердцевина"]
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_Has1Anagram_ingoreDigits():
    array = [12, "Сон", 21, "Нос"]
    ER = ["Сон", "Нос"]
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_Has2Anagram_ingoreSpecials():
    array = ["дозревание", 12, "древЕсница", None, "сердцевина", False, "раздвоение"]
    ER = ["дозревание", "древЕсница", "сердцевина", "раздвоение"]
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_EmptyArray():
    array = []
    ER = []
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_NoAnagram1():
    array = ["творог", "СОКОЛ", "носок"]
    ER = []
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_NoAnagram2():
    # не то, чем кажется
    array = ["древесницA", "cердцевинA"]
    ER = []
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_NoAnagram3():
    array = [1, 2, 3]
    ER = []
    AR = getAnagram(array)
    assert set(ER) == set(AR)

def test_СheckСaseOfLetters():
    array = ["НОС"]
    failER = ["нос"]
    ER = ["НОС"]
    AR = getAnagram(array)
    assert not (set(AR) == set(failER))
    assert set(AR) == set(ER)