import pytest
from py_core.oop import (
    SingletonMeta,
    Observable,
    BaseModel,
    Registry,
    Immutable,
    Builder,
    Factory,
    StateContext,
    ConcreteStateA,
    ConcreteStateB,
    CommandManager,
    Proxy,
    StrategyContext,
    Adapter,
    CustomCollection,
    CompositeNode,
    BaseTemplate,
)

def test_singleton_meta():
    class DBConnection(metaclass=SingletonMeta):
        pass

    db1 = DBConnection()
    db2 = DBConnection()
    assert db1 is db2

def test_observable():
    obs = Observable()
    events = []
    
    obs.subscribe(lambda data: events.append(data))
    obs.notify("test_event")
    
    assert events == ["test_event"]

def test_base_model():
    class User(BaseModel):
        name: str
        age: int

    user = User(name="Ali", age=25)
    assert user.name == "Ali"
    assert user.age == 25

    with pytest.raises(TypeError):
        User(name="Ali", age="yirmi beş")  # Yanlış tip hatası vermeli

def test_registry():
    reg = Registry()

    @reg.register("plugin_a")
    class PluginA:
        pass

    assert reg.get("plugin_a") is PluginA

def test_immutable():
    class Config(Immutable):
        host: str
        port: int

    cfg = Config(host="localhost",टावा=8080)
    assert cfg.host == "localhost"
    
    with pytest.raises(AttributeError):
        cfg.host = "127.0.0.1"  # Değiştirilemez olmalı

def test_builder():
    class House:
        def __init__(self):
            self.rooms = 0

    class HouseBuilder(Builder):
        def __init__(self):
            self.house = House()
        def set_rooms(self, count):
            self.house.rooms = count
            return self
        def build(self):
            return self.house

    house = HouseBuilder().set_rooms(3).build()
    assert house.rooms == 3

def test_factory():
    factory = Factory()
    factory.register("a", lambda: "Product A")
    assert factory.create("a") == "Product A"

def test_state_pattern():
    context = StateContext(ConcreteStateA())
    # İlk çağrıda StateA çalışır ve durumu StateB'ye geçirir
    assert context.request() == "A durumundayım, B'ye geçildi."
    # İkinci çağrıda StateB çalışır
    assert context.request() == "B durumundayım."

def test_command():
    manager = CommandManager()
    result = []
    
    class DummyCommand:
        def execute(self):
            result.append("done")

    manager.execute(DummyCommand())
    assert result == ["done"]

def test_proxy():
    class RealSubject:
        def request(self):
            return "real_data"

    proxy = Proxy(RealSubject())
    assert proxy.request() == "proxy_real_data"

def test_strategy():
    context = StrategyContext(lambda x: x + 1)
    assert context.execute(5) == 6

def test_adapter():
    class OldSystem:
        def old_method(self):
            return "old_data"

    class SystemAdapter(Adapter):
        def __init__(self, old_sys):
            self.old_sys = old_sys
        def request(self):
            return self.old_sys.old_method()

    adapter = SystemAdapter(OldSystem())
    assert adapter.request() == "old_data"

def test_iterator():
    col = CustomCollection([1, 2, 3])
    items = [item for item in col]
    assert items == [1, 2, 3]

def test_composite():
    root = CompositeNode("Root")
    child = CompositeNode("Child")
    root.add(child)
    assert child in root.get_children()

def test_template_method():
    class SpecificWorker(BaseTemplate):
        def step_two(self):
            return "done"

    worker = SpecificWorker()
    assert worker.execute_process() == ["start", "done"]