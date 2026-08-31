import time
import functools
import os
import sys
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

def rate_limit(min_interval: float) -> Callable:
    """Fonksiyonun minimum çağrı aralığını sınırlar (rate limiting)."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        last_called = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.perf_counter()
            if now - last_called < min_interval:
                raise RuntimeError("Rate limit aşıldı!")
            last_called = now
            return func(*args, **kwargs)
        return wrapper
    return decorator

def singleton(cls: Type[Any]) -> Callable[..., Any]:
    """Bir sınıfın yalnızca tek bir örneğinin (instance) oluşturulmasını sağlar."""
    instances = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

def log_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyon çağrılarını argümanları ve sonuçlarıyla birlikte loglar."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Çalıştırılıyor: {func.__name__} | args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Tamamlandı: {func.__name__} | sonuç: {result}")
        return result
    return wrapper

@contextmanager
def temp_env(**kwargs: str):
    """Geçici ortam değişkenleri tanımlar, blok bitince eski haline getirir."""
    old_values = {}
    for key, value in kwargs.items():
        old_values[key] = os.environ.get(key)
        os.environ[key] = value
    try:
        yield
    finally:
        for key, value in old_values.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value

@contextmanager
def redirect_stdout(new_target):
    """Standart çıktıyı (stdout) geçici olarak başka bir akışa yönlendirir."""
    old_target = sys.stdout
    sys.stdout = new_target
    try:
        yield new_target
    finally:
        sys.stdout = old_target