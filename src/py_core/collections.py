from typing import List

def get_evens(numbers: List[int]) -> List[int]:
    """Verilen sayı listesindeki çift sayıları filtreleyerek döndürür."""
    return [num for num in numbers if num % 2 == 0]