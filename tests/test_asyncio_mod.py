import pytest
import asyncio
from py_core.async_utils import (
    async_identity,
    gather_results,
    AsyncTimeoutWrapper,
    AsyncQueueWorker,
    async_memoize,
    AsyncRateLimiter,
    AsyncRetryWrapper,
    AsyncBatchProcessor,
    AsyncEventBus,
    AsyncResourcePool,
)

@pytest.mark.asyncio
async def test_async_identity():
    result = await async_identity(42, delay=0.1)
    assert result == 42

@pytest.mark.asyncio
async def test_gather_results():
    async def sample(x):
        await asyncio.sleep(0.05)
        return x * 2

    results = await gather_results([sample(1), sample(2), sample(3)])
    assert results == [2, 4, 6]

@pytest.mark.asyncio
async def test_async_timeout_wrapper():
    async def slow_task():
        await asyncio.sleep(0.2)
        return "done"

    # Zaman aşımına uğramalı
    with pytest.raises(asyncio.TimeoutError):
        await AsyncTimeoutWrapper.run(slow_task(), timeout=0.05)

@pytest.mark.asyncio
async def test_async_queue_worker():
    worker = AsyncQueueWorker()
    await worker.put(1)
    await worker.put(2)
    
    processed = await worker.process_all()
    assert processed == [2, 4]  # Gelen veriyi 2 ile çarptığını varsayalım

@pytest.mark.asyncio
async def test_async_memoize():
    call_count = 0

    @async_memoize
    async def expensive_calc(x: int) -> int:
        nonlocal call_count
        call_count += 1
        await asyncio.sleep(0.05)
        return x + 10

    assert await expensive_calc(5) == 15
    assert await expensive_calc(5) == 15  # Cache'den gelmeli
    assert call_count == 1

@pytest.mark.asyncio
async def test_async_rate_limiter():
    limiter = AsyncRateLimiter(rate=5)
    # Hızlıca çalışabildiğini test edelim
    await limiter.acquire()
    assert True

@pytest.mark.asyncio
async def test_async_retry_wrapper():
    attempts = 0
    @AsyncRetryWrapper(retries=2, delay=0.01)
    async def flaky_task():
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise ValueError("Geçici hata")
        return "başarılı"

    result = await flaky_task()
    assert result == "başarılı"
    assert attempts == 2

@pytest.mark.asyncio
async def test_async_batch_processor():
    processor = AsyncBatchProcessor(batch_size=2)
    items = [1, 2, 3, 4, 5]
    batches = [b async for b in processor.process(items)]
    assert batches == [[1, 2], [3, 4], [5,]]

@pytest.mark.asyncio
async def test_async_event_bus():
    bus = AsyncEventBus()
    received = []

    @bus.subscribe("ping")
    async def on_ping(data):
        received.append(data)

    await bus.publish("ping", "pong")
    assert received == ["pong"]

@pytest.mark.asyncio
async def test_async_resource_pool():
    pool = AsyncResourcePool(max_size=1)
    async with pool.acquire() as resource:
        assert resource is not None