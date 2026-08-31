from typing import Any, Callable, Dict, Type

class SingletonMeta(type):
    """Metaclass tabanlı Singleton tasarım kalıbı."""
    _instances: Dict[Type[Any], Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Observable:
    """Observer (Gözlemci) tasarım kalıbı implementasyonu."""
    def __init__(self):
        self._listeners: list[Callable[[Any], None]] = []

    def subscribe(self, callback: Callable[[Any], None]) -> None:
        self._listeners.append(callback)

    def unsubscribe(self, callback: Callable[[Any], None]) -> None:
        self._listeners.remove(callback)

    def notify(self, data: Any) -> None:
        for listener in self._listeners:
            listener(data)

class BaseModel:
    """Alan tiplerini doğrulayan basit bir veri modeli."""
    def __init__(self, **kwargs):
        annotations = getattr(self, "__annotations__", {})
        for field, expected_type in annotations.items():
            value = kwargs.get(field)
            if value is not None and not isinstance(value, expected_type):
                raise TypeError(f"'{field}' alanı {expected_type} tipinde olmalı, {type(value)} geldi.")
            setattr(self, field, value)

class Registry:
    """Sınıf ve fonksiyonları merkezi olarak kaydeden kayıt defteri."""
    def __init__(self):
        self._items: Dict[str, Any] = {}

    def register(self, name: str) -> Callable[[Any], Any]:
        def decorator(cls_or_func: Any) -> Any:
            self._items[name] = cls_or_func
            return cls_or_func
        return decorator

    def get(self, name: str) -> Any:
        if name not in self._items:
            raise KeyError(f"'{name}' kayıt defterinde bulunamadı.")
        return self._items[name]

class Immutable:
    """Özellikleri sonradan değiştirilemeyen (read-only) nesne tabanı."""
    def __init__(self, **kwargs):
        super().__setattr__("_data", kwargs)
        annotations = getattr(self, "__annotations__", {})
        for field in annotations:
            if field in kwargs:
                super().__setattr__(field, kwargs[field])

    def __setattr__(self, key, value):
        raise AttributeError("Immutable nesnelerin özellikleri değiştirilemez!")

class Builder:
    """Karmaşık nesnelerin adım adım oluşturulmasını sağlayan temel sınıf."""
    def build(self) -> Any:
        raise NotImplementedError

class Factory:
    """Koşullara veya anahtarlara göre nesne üreten fabrika sınıfı."""
    def __init__(self):
        self._creators: Dict[str, Callable[[], Any]] = {}

    def register(self, key: str, creator: Callable[[], Any]) -> None:
        self._creators[key] = creator

    def create(self, key: str) -> Any:
        if key not in self._creators:
            raise KeyError(f"'{key}' için kayıtlı bir üretici bulunamadı.")
        return self._creators[key]()

class State:
    """Tüm durum sınıfları için soyut taban sınıf."""
    def handle(self, context: Any) -> str:
        raise NotImplementedError

class ConcreteStateA(State):
    """Durum A: Çalıştığında durumu B'ye çevirir."""
    def handle(self, context: Any) -> str:
        context.set_state(ConcreteStateB())
        return "A durumundayım, B'ye geçildi."

class ConcreteStateB(State):
    """Durum B: Son durum davranışı."""
    def handle(self, context: Any) -> str:
        return "B durumundayım."

class StateContext:
    """Durum (State) kalıbını yöneten ana bağlam sınıfı."""
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def request(self) -> str:
        return self._state.handle(self)

class CommandManager:
    """Komutları sıraya koyan ve çalıştıran yönetici."""
    def __init__(self):
        self._history = []

    def execute(self, command: Any) -> None:
        command.execute()
        self._history.append(command)

class Proxy:
    """Gerçek nesneye erişimi kontrol eden veya araya katman koyan Proxy sınıfı."""
    def __init__(self, real_subject: Any):
        self._real_subject = real_subject

    def request(self) -> str:
        return f"proxy_{self._real_subject.request()}"

class StrategyContext:
    """Strateji (Strategy) kalıbı bağlam sınıfı."""
    def __init__(self, strategy: Callable[[Any], Any]):
        self._strategy = strategy

    def set_strategy(self, strategy: Callable[[Any], Any]):
        self._strategy = strategy

    def execute(self, data: Any) -> Any:
        return self._strategy(data)

class Adapter:
    """Farklı arayüzleri birbirine uyarlayan adaptör sınıfı."""
    def request(self) -> str:
        raise NotImplementedError

class CustomCollection:
    """Özel iterator desteği sunan koleksiyon sınıfı."""
    def __init__(self, items: list):
        self._items = items

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration

class CompositeNode:
    """Ağaç yapısındaki parça-bütün ilişkilerini yöneten Composite sınıfı."""
    def __init__(self, name: str):
        self.name = name
        self._children = []

    def add(self, node: 'CompositeNode'):
        self._children.append(node)

    def get_children(self):
        return self._children

class BaseTemplate:
    """Algoritma iskeletini tanımlayan Template Method temel sınıfı."""
    def step_one(self):
        return "start"

    def step_two(self):
        raise NotImplementedError

    def execute_process(self) -> list:
        return [self.step_one(), self.step_two()]