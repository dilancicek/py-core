def count_vowels(text: str) -> int:
    vowels = "aeıioöuüAEIİOÖUÜ"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text: str) -> bool:
    """
    Verilen metnin palindrom olup olmadığını kontrol eder.
    Boşlukları yok sayar ve büyük/küçük harf duyarsızdır.
    """
    temiz_metin = text.replace(" ", "").lower()
    return temiz_metin == temiz_metin[::-1]

def reverse_words(sentence: str) -> str:
    """Cümledeki kelimelerin sırasını tersine çevirir."""
    return " ".join(sentence.split()[::-1])

def remove_vowels(text: str) -> str:
    """Metindeki sesli harfleri tamamen çıkarır."""
    vowels = "aeıioöuüAEIİOÖUÜ"
    return "".join(char for char in text if char not in vowels)

def to_snake_case(text: str) -> str:
    """Metni snake_case (alt_tireli) formata dönüştürür."""
    # split() fazladan boşlukları temizler, join() ve lower() ile birleştiririz.
    return "_".join(text.split()).lower()