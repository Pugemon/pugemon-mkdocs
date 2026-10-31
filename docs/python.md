# Python

Пример страницы для Python-проекта.

```python title="sensor.py"
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Sensor:
    """Датчик температуры на шине I2C."""

    bus: int
    address: int = 0x48

    def read_celsius(self) -> float:
        raw = Path(f"/sys/bus/i2c/devices/{self.bus}-00{self.address:x}/temp1_input")
        return int(raw.read_text()) / 1000  # миллиградусы → градусы


if __name__ == "__main__":
    print(f"{Sensor(bus=1).read_celsius():.1f} °C")
```

## Одно и то же на трёх языках

=== "Python"

    ```python
    def greet(name: str) -> str:
        return f"Привет, {name}!"
    ```

=== "C++"

    ```cpp
    std::string greet(const std::string& name) {
        return "Привет, " + name + "!";
    }
    ```

=== "Go"

    ```go
    func Greet(name string) string {
        return "Привет, " + name + "!"
    }
    ```

!!! tip "API-справка"
    Для автогенерации справки из docstring подключите `mkdocstrings[python]`, стили для неё в теме уже есть.
