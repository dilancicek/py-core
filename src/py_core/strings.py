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

def count_words(text: str) -> int:
    """Metindeki kelime sayısını döndürür."""
    return len(text.split())

def is_anagram(word1: str, word2: str) -> bool:
    """İki kelimenin anagram (aynı harflerden oluşma) olup olmadığını kontrol eder."""
    return sorted(word1.replace(" ", "").lower()) == sorted(word2.replace(" ", "").lower())

def longest_word(text: str) -> str:
    """Metindeki en uzun kelimeyi bulur."""
    words = text.split()
    return max(words, key=len) if words else ""

def count_char(text: str, char: str) -> int:
    """Metin içinde belirli bir karakterin (büyük/küçük harf duyarsız) kaç kez geçtiğini bulur."""
    return text.lower().count(char.lower())

def truncate(text: str, max_length: int) -> str:
    """Metni belirtilen uzunlukta keser ve sonuna '...' ekler."""
    return text[:max_length] + "..." if len(text) > max_length else text