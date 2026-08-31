from typing import List, Any, Union, Optional, Dict

def get_evens(numbers: List[int]) -> List[int]:
    """Verilen sayı listesindeki çift sayıları filtreleyerek döndürür."""
    return [num for num in numbers if num % 2 == 0]

def get_unique_elements(items: List[Any]) -> List[Any]:
    """Listedeki tekrar eden elemanları kaldırır, orijinal sırayı korur."""
    return list(dict.fromkeys(items))

def find_max(numbers: List[int]) -> Union[int, None]:
    """Verilen sayı listesindeki en büyük elemanı bulur, liste boşsa None döndürür."""
    return max(numbers) if numbers else None

def flatten_list(nested_list: list) -> list:
    """İç içe geçmiş listeleri tek boyutlu düz bir liste haline getirir."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def find_min(numbers: List[int]) -> Union[int, None]:
    """Verilen sayı listesindeki en küçük elemanı bulur, liste boşsa None döndürür."""
    return min(numbers) if numbers else None

def calculate_average(numbers: List[int]) -> Optional[float]:
    """Verilen sayı listesinin aritmetik ortalamasını hesaplar, liste boşsa None döndürür."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def count_frequencies(items: List[Any]) -> Dict[Any, int]:
    """Listedeki her elemanın kaç kez tekrar ettiğini bir sözlük olarak döndürür."""
    frequency_map = {}
    for item in items:
        frequency_map[item] = frequency_map.get(item, 0) + 1
    return frequency_map

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Bir listeyi belirtilen boyutta küçük parçalara (alt listelere) böler."""
    if size <= 0:
        return []
    return [items[i:i + size] for i in range(0, len(items), size)]

def merge_dicts(dict1: Dict[Any, int], dict2: Dict[Any, int]) -> Dict[Any, int]:
    """İki sözlüğü birleştirir, ortak anahtarların değerlerini toplar."""
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result