from collections import deque
from typing import Any, Iterable, Iterator, List, Union, Callable

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

def windowed(iterable: Iterable[Any], size: int, step: int = 1) -> Iterator[List[Any]]:
    """Belirtilen boyut ve adım aralığıyla (step) lazy pencereler üretir."""
    if size <= 0 or step <= 0:
        return
    
    items = list(iterable)
    for i in range(0, len(items) - size + 1, step):
        yield items[i : i + size]

def drop_while_value(predicate: Callable[[Any], bool], iterable: Iterable[Any]) -> Iterator[Any]:
    """Koşul doğru olduğu sürece elemanları atlar, ilk yanlış koşuldan itibaren üretir."""
    iterator = iter(iterable)
    dropping = True
    for item in iterator:
        if dropping:
            if not predicate(item):
                dropping = False
                yield item
        else:
            yield item

def take_until(predicate: Callable[[Any], bool], iterable: Iterable[Any]) -> Iterator[Any]:
    """Koşul sağlanana kadar elemanları üretir, koşul sağlandığında durur."""
    for item in iterable:
        if predicate(item):
            break
        yield item

class peekable:
    """Bir iteratöre tüketmeden sıradaki elemana bakma (peek) özelliği kazandırır."""
    def __init__(self, iterable: Iterable[Any]):
        self._iterator = iter(iterable)
        self._has_peeked = False
        self._peeked_value = None

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self._has_peeked:
            self._has_peeked = False
            val = self._peeked_value
            self._peeked_value = None
            return val
        return next(self._iterator)

    def peek(self, default: Any = None) -> Any:
        """İteratörü ilerletmeden sıradaki elemanı döndürür."""
        if not self._has_peeked:
            try:
                self._peeked_value = next(self._iterator)
                self._has_peeked = True
            except StopIteration:
                return default
        return self._peeked_value

def pairwise(iterable: Iterable[Any]) -> Iterator[tuple]:
    """Bir akıştaki ardışık elemanları ikili demetler (tuple) halinde üretir."""
    iterator = iter(iterable)
    try:
        prev = next(iterator)
    except StopIteration:
        return

    for item in iterator:
        yield (prev, item)
        prev = item
