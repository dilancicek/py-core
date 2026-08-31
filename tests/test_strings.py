from py_core.strings import count_vowels, is_palindrome, reverse_words, remove_vowels, to_snake_case

def test_count_vowels():
    assert count_vowels("Merhaba") == 3
    assert count_vowels("Yazılım Mühendisliği") == 8
    assert count_vowels("PYThOn") == 1
    assert count_vowels("bcdfgh") == 0
    assert count_vowels("") == 0

def test_is_palindrome():
    assert is_palindrome("Kavak") == True
    assert is_palindrome("Ey Edip Adanada pide ye") == True
    assert is_palindrome("Merhaba") == False
    assert is_palindrome("") == True
    assert is_palindrome("12321") == True

def test_reverse_words():
    assert reverse_words("Merhaba Dünya") == "Dünya Merhaba"
    assert reverse_words("Python harika bir dil") == "dil bir harika Python"
    assert reverse_words("  boşluklu   metin  ") == "metin boşluklu"
    assert reverse_words("") == ""

def test_remove_vowels():
    assert remove_vowels("Merhaba") == "Mrhb"
    assert remove_vowels("Python") == "Pythn"
    assert remove_vowels("AEIİOÖUÜ") == ""

def test_to_snake_case():
    assert to_snake_case("Hello World") == "hello_world"
    assert to_snake_case("Python Programlama Dili") == "python_programlama_dili"
    assert to_snake_case("zaten_snake_case") == "zaten_snake_case"