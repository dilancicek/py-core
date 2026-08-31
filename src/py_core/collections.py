from typing import List, Any, Union

def get_evens(numbers: List[int]) -> List[int]:
    """Verilen sayı listesindeki çift sayıları filtreleyerek döndürür."""
    return [num for num in numbers if num % 2 == 0]

def get_unique_elements(items: List[Any]) -> List[Any]:
    """Listedeki tekrar eden elemanları kaldırır, orijinal sırayı korur."""
    return list(dict.fromkeys(items))

def find_max(numbers: List[int]) -> Union[int, None]:
    """Verilen sayı listesindeki en büyük elemanı bulur, liste boşsa None döndürür."""
    return max(numbers) if numbers else None