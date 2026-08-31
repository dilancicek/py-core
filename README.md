# Py-Core Library 🚀

`py_core`, Python'da modern yazılım geliştirme prensipleri (TDD, OOP, Type Safety ve Asenkron Programlama) gözetilerek sıfırdan geliştirilmiş kapsamlı bir çekirdek kütüphanedir.

## 📁 Modüller ve Yapı

Kütüphane içerisinde toplam **80 adetim birim test (pytest)** ile test edilmiş 6 ana modül bulunmaktadır:

1. **Collections (`collections_utils.py`)**: Gelişmiş veri yapıları ve koleksiyon manipülasyonları.
2. **Strings (`strings.py`)**: Metin işleme, biçimlendirme ve doğrulama araçları.
3. **Generators (`generators.py`)**: Bellek dostu veri akışları ve özel jeneratör yapıları.
4. **Decorators & Context Managers (`decorators.py`)**: Fonksiyon davranışı yönetimi ve bağlam yöneticileri.
5. **OOP Design Patterns (`oop.py`)**: Yazılım tasarım kalıpları (Singleton, Factory, State, Strategy, Observer, vb.).
6. **Typing & Async (`typing_utils.py`, `async_utils.py`)**: Tip güvenliği, protokoller ve asenkron işlem yöneticileri.

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel ortamınızda çalıştırmak için **uv** paket yöneticisini kullanabilirsiniz:

```bash
# Bağımlılıkları yükleyin
uv sync

# Testleri çalıştırın
uv run pytest