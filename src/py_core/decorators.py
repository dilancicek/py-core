import time
import functools
from contextlib import contextmanager
from typing import Any, Callable, Type, Tuple

def time_it(func: Callable[..., Any]) -> Callable[..., Tuple[Any, float]]:
    """Fonksiyonun çalışma süresini ölçer ve (sonuç, süre) ikilisi döndürür."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper

def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    """Hata alan fonksiyonu belirtilen sayıda yeniden dener."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyon sonuçlarını önbelleğe alır."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@contextmanager
def suppress_exception(*exceptions: Type[Exception]):
    """Belirtilen exception'ları güvenli bir şekilde bastırır."""
    try:
        yield
    except exceptions:
        pass

class TimerContext:
    def __init__(self):
        self.duration = 0.0
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration = time.perf_counter() - self.start

def timer_context():
    """Kod bloğunun süresini ölçen context manager."""
    return TimerContext()