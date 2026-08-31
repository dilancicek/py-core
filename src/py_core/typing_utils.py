from typing import Any, Callable, Type, TypeVar, Union, Protocol, runtime_checkable
from typing_extensions import TypeAlias

JSON: TypeAlias = Union[
    str, int, float, bool, None, 
    list["JSON"], 
    dict[str, "JSON"]
]

T = TypeVar("T")
Predicate: TypeAlias = Callable[[T], bool]

@runtime_checkable
class HasName(Protocol):
    name: str

py_core_typing = Any
def is_of_type(value: Any, expected_type: Type[Any]) -> bool:
    """Verilen değerin belirtilen tip ile uyumlu olup olmadığını kontrol eder."""
    origin = getattr(expected_type, "__origin__", None)
    
    if origin is list:
        if not isinstance(value, list):
            return False
        args = getattr(expected_type, "__args__", (Any,))
        return all(is_of_type(item, args[0]) for item in value)
        
    if origin is dict:
        if not isinstance(value, dict):
            return False
        return all(isinstance(k, str) for k in value.keys())

    try:
        return isinstance(value, expected_type)
    except TypeError:
        return True

T_co = TypeVar("T_co")
def safe_cast(value: Any, target_type: Type[T_co], default: Any = None) -> Any:
    """Değeri güvenli bir şekilde hedeflenen tipe dönüştürür, hata durumunda default döner."""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default

def maybe(value: Any, cast_type: Type[T], default: T) -> T:
    """Değer None veya geçersizse default döner, aksi halde cast eder."""
    if value is None:
        return default
    try:
        return cast_type(value)
    except (ValueError, TypeError):
        return default

class Result:
    """Başarı veya hata durumunu tip güvenli yöneten Result sınıfı."""
    def __init__(self, value: Any = None, error: Any = None, success: bool = True):
        self._value = value
        self._error = error
        self._success = success

    @classmethod
    def Ok(cls, value: Any) -> "Result":
        return cls(value=value, success=True)

    @classmethod
    def Err(cls, error: Any) -> "Result":
        return cls(error=error, success=False)

    def is_ok(self) -> bool:
        return self._success

    def is_err(self) -> bool:
        return not self._success

    def unwrap(self) -> Any:
        if not self._success:
            raise ValueError(f"Result Hata içeriyor: {self._error}")
        return self._value

    def unwrap_or(self, default: Any) -> Any:
        return self._value if self._success else default

class TypeValidator:
    """Verilen bir sözlükteki verilerin tiplerini şemaya göre doğrulayan sınıf."""
    def __init__(self, schema: dict[str, Type[Any]]):
        self._schema = schema

    def validate(self, data: dict[str, Any]) -> bool:
        for field, expected_type in self._schema.items():
            if field not in data:
                raise KeyError(f"'{field}' alanı eksik.")
            value = data[field]
            if not isinstance(value, expected_type):
                raise TypeError(f"'{field}' alanı {expected_type} tipinde olmalı, {type(value)} geldi.")
        return True

class ImmutableList:
    """Elemanları sonradan değiştirilemeyen tip güvenli liste."""
    def __init__(self, items: list[Any]):
        self._items = tuple(items)

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def append(self, item: Any):
        raise TypeError("ImmutableList öğeleri değiştirilemez veya eklenemez!")

class CallableRegistry:
    """Sadece callable nesneleri kaydeden güvenli kayıt defteri."""
    def __init__(self):
        self._registry: dict[str, Callable[..., Any]] = {}

    def register(self, name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            if not callable(func):
                raise TypeError("Kayıt edilen nesne bir fonksiyon/callable olmalıdır.")
            self._registry[name] = func
            return func
        return decorator

    def get(self, name: str) -> Callable[..., Any]:
        if name not in self._registry:
            raise KeyError(f"'{name}' kayıt defterinde bulunamadı.")
        return self._registry[name]