# C++

Пример страницы для C++-проекта.

```cpp title="tmp102.cpp" linenums="1"
#include <cstdint>
#include <fstream>
#include <string>

namespace pugemon {

constexpr std::uint8_t kDefaultAddress = 0x48;

class Tmp102 {
public:
    explicit Tmp102(int bus, std::uint8_t address = kDefaultAddress)
        : bus_(bus), address_(address) {}

    double read_celsius() const {
        std::ifstream in(path());
        long millis = 0;
        in >> millis;
        return millis / 1000.0;  // миллиградусы → градусы
    }

private:
    std::string path() const;
    int bus_;
    std::uint8_t address_;
};

}  // namespace pugemon
```

```diff
- reg = <0x49>;
+ reg = <0x48>;
```
