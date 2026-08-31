import time
import pytest
import os
import sys
import io
from py_core.decorators import (
    time_it,
    retry,
    memoize,
    suppress_exception,
    timer_context,
    rate_limit,
    singleton,
    log_execution,
    temp_env,
    redirect_stdout,
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

def test_rate_limit():
    @rate_limit(min_interval=0.05)
    def fast_call():
        return "ok"

    assert fast_call() == "ok"
    # Çok hızlı ikinci çağrıda exception fırlatmalı
    import pytest
    with pytest.raises(Exception):
        fast_call()

def test_singleton():
    @singleton
    class Database:
        def __init__(self):
            self.id = 123

    db1 = Database()
    db2 = Database()
    assert db1 is db2

def test_log_execution(capsys):
    @log_execution
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert "add" in captured.out

def test_temp_env():
    os.environ["TEST_VAR"] = "old_val"
    with temp_env(TEST_VAR="new_val"):
        assert os.environ["TEST_VAR"] == "new_val"
    assert os.environ["TEST_VAR"] == "old_val"

def test_redirect_stdout():
    f = io.StringIO()
    with redirect_stdout(f):
        print("Hello World")
    assert "Hello World" in f.getvalue()