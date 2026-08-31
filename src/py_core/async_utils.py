import asyncio
from typing import Any, Callable, Coroutine, List

async def async_identity(value: Any, delay: float = 0.0) -> Any:
    """Verilen değeri belirtilen gecikme ile asenkron olarak döndürür."""
    if delay > 0:
        await asyncio.sleep(delay)
    return value

async def gather_results(tasks: List[Coroutine[Any, Any, Any]]) -> List[Any]:
    """Birden fazla coroutine'i aynı anda çalıştırıp sonuçlarını toplar."""
    return await asyncio.gather(*tasks)

class AsyncTimeoutWrapper:
    """Asenkron görevler için zaman aşımı yönetimi sağlar."""
    @staticmethod
    async def run(coro: Coroutine[Any, Any, Any], timeout: float) -> Any:
        return await asyncio.wait_for(coro, timeout=timeout)

class AsyncQueueWorker:
    """Asenkron kuyruk tabanlı basit bir işçi sınıfı."""
    def __init__(self):
        self._queue: asyncio.Queue = asyncio.Queue()

    async def put(self, item: Any):
        await self._queue.put(item)

    async def process_all(self) -> List[Any]:
        results = []
        while not self._queue.empty():
            item = await self._queue.get()
            results.setItem if hasattr(results, "setItem") else results.append(item * 2)
            self._queue.task_done()
        return results

def async_memoize(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Coroutine[Any, Any, Any]]:
    """Asenkron fonksiyonlar için basit bir önbellek (memoization) dekoratörü."""
    cache = {}

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = await func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

class AsyncRateLimiter:
    """Asenkron işlemler için basit bir hız sınırlayıcı."""
    def __init__(self, rate: float):
        self._rate = rate
        self._last_time = 0.0

    async def acquire(self):
        now = asyncio.get_event_loop().time()
        elapsed = now - self._last_time
        wait_time = (1.0 / self._rate) - elapsed
        if wait_time > 0:
            await asyncio.sleep(wait_time)
        self._last_time = asyncio.get_event_loop().time()

def AsyncRetryWrapper(retries: int = 3, delay: float = 0.1):
    """Hata alan asenkron fonksiyonları tekrar deneme dekoratörü."""
    def decorator(func: Callable[..., Coroutine[Any, Any, Any]]):
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        await asyncio.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

class AsyncBatchProcessor:
    """Verileri asenkron olarak gruplar halinde işleyen sınıf."""
    def __init__(self, batch_size: int):
        self._batch_size = batch_size

    async def process(self, items: list[Any]):
        for i in range(0, len(items), self._batch_size):
            yield items[i:i + self._batch_size]
            await asyncio.sleep(0.01)

class AsyncEventBus:
    """Asenkron olay (event) yayın ve dinleme yöneticisi."""
    def __init__(self):
        self._listeners: dict[str, list[Callable[..., Coroutine[Any, Any, Any]]]] = {}

    def subscribe(self, event_name: str):
        def decorator(func: Callable[..., Coroutine[Any, Any, Any]]):
            if event_name not in self._listeners:
                self._listeners[event_name] = []
            self._listeners[event_name].append(func)
            return func
        return decorator

    async def publish(self, event_name: str, data: Any):
        if event_name in self._listeners:
            for listener in self._listeners[event_name]:
                await listener(data)

class AsyncResourcePool:
    """Sınırlı sayıda kaynağı asenkron yöneten havuz."""
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._semaphore = asyncio.Semaphore(max_size)

    class _ResourceContext:
        def __init__(self, semaphore: asyncio.Semaphore):
            self._semaphore = semaphore

        async def __aenter__(self):
            await self._semaphore.acquire()
            return "ResourceInstance"

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            self._semaphore.release()

    def acquire(self):
        return self._ResourceContext(self._semaphore)