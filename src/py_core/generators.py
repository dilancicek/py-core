from collections import deque
from typing import Any, Iterable, Iterator, List, Union

def chunk_generator(iterable: Iterable[Any], size: int) -> Iterator[List[Any]]:
    """Bir iterable'ı tüketmeden, belirtilen boyutta küçük parçalar halinde (lazy) üretir."""
    if size <= 0:
        raise ValueError("Chunk boyutu 0'dan büyük olmalıdır.")
    
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def running_average(iterable: Iterable[Union[int, float]]) -> Iterator[float]:
    """Bir sayı akışının kümülatif ortalamasını her adımda lazy olarak hesaplar ve üretir."""
    total = 0.0
    count = 0
    for item in iterable:
        total += item
        count += 1
        yield total / count

def unique_everseen(iterable: Iterable[Any]) -> Iterator[Any]:
    """Bir iterable içindeki elemanların sırasını bozmadan sadece benzersiz olanları lazy olarak üretir."""
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

def sliding_window(iterable: Iterable[Any], size: int) -> Iterator[List[Any]]:
    """Belirtilen boyutta kayan bir pencere (sliding window) oluşturarak lazy üretir."""
    if size <= 0:
        return
    
    iterator = iter(iterable)
    window = deque(maxlen=size)
    
    # İlk pencereyi doldur
    for _ in range(size):
        try:
            window.append(next(iterator))
        except StopIteration:
            return
            
    yield list(window)
    
    # Geri kalan elemanları kaydırarak devam et
    for item in iterator:
        window.append(item)
        yield list(window)

def flatten_generator(iterable_of_iterables: Iterable[Iterable[Any]]) -> Iterator[Any]:
    """İç içe geçmiş iterable yapılarını tek seviyede lazy olarak düzleştirir."""
    for sublist in iterable_of_iterables:
        for item in sublist:
            yield item

