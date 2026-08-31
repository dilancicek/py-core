import pytest
from typing import Dict, List, Any
from py_core.typing_utils import (
    is_of_type,
    JSON,
    Predicate,
    safe_cast,
    HasName,
    maybe,
    Result,
    TypeValidator,
    ImmutableList,
    CallableRegistry,
)

def test_is_of_type():
    assert is_of_type(5, int) is True
    assert is_of_type("hello", int) is False
    assert is_of_type([1, 2, 3], List[int]) is True

def test_json_alias():
    data: JSON = {"key": [1, 2, {"nested": "val"}]}
    assert isinstance(data, dict)

def test_predicate():
    is_even: Predicate[int] = lambda x: x % 2 == 0
    assert is_even(4) is True
    assert is_even(5) is False

def test_safe_cast():
    assert safe_cast("123", int) == 123
    assert safe_cast("abc", int, default=0) == 0

def test_protocol_has_name():
    class Person:
        def __init__(self, name: str):
            self.name = name

    p = Person("Ali")
    assert isinstance(p, HasName)

def test_maybe():
    assert maybe(None, int, 42) == 42
    assert maybe("10", int, 0) == 10

def test_result_monad():
    res_ok = Result.Ok(5)
    assert res_ok.is_ok() is True
    assert res_ok.unwrap() == 5

    res_err = Result.Err("Hata")
    assert res_err.is_err() is True
    assert res_err.unwrap_or(0) == 0

def test_type_validator():
    validator = TypeValidator({"name": str, "age": int})
    
    # Doğru tip verileri
    assert validator.validate({"name": "Ali", "age": 25}) is True
    
    # Yanlış tip verileri
    import pytest
    with pytest.raises(TypeError):
        validator.validate({"name": "Ali", "age": "yirmi beş"})

def test_immutable_list():
    lst = ImmutableList([1, 2, 3])
    assert lst[0] == 1
    import pytest
    with pytest.raises(TypeError):
        lst.append(4)  # Değiştirilemez olmalı

def test_callable_registry():
    reg = CallableRegistry()
    @reg.register("add")
    def add(a: int, b: int) -> int:
        return a + b

    assert reg.get("add")(2, 3) == 5