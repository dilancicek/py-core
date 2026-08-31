import time
import pytest
from py_core.decorators import (
    time_it,
    retry,
    memoize,
    suppress_exception,
    timer_context,
)

def test_time_it():
    @time_it
    def dummy():
        return "ok"
    
    res, duration = dummy()
    assert res == "ok"
    assert isinstance(duration, float)

def test_retry():
    attempts = 0
    @retry(retries=3, delay=0.01)
    def flaky():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Fail")
        return "success"

    assert flaky() == "success"
    assert attempts == 3

def test_memoize():
    call_count = 0
    @memoize
    def compute(x):
        nonlocal call_count
        call_count += 1
        return x * 2

    assert compute(5) == 10
    assert compute(5) == 10
    assert call_count == 1  # İkinci çağrıda cache'den gelmeli

def test_suppress_exception():
    with suppress_exception(ValueError):
        raise ValueError("Hata bastırıldı")

def test_timer_context():
    with timer_context() as t:
        time.sleep(0.01)
    assert t.duration > 0