from py_core.strings import count_vowels

def test_count_vowels():
    assert count_vowels("Merhaba") == 3
    assert count_vowels("Yazılım Mühendisliği") == 8
    assert count_vowels("PYThOn") == 1
    assert count_vowels("bcdfgh") == 0
    assert count_vowels("") == 0