# Go

Пример страницы для Go-проекта.

```go title="sensor.go"
package sensor

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const DefaultAddress = 0x48

// ReadCelsius читает температуру датчика из sysfs.
func ReadCelsius(bus int, addr uint8) (float64, error) {
	path := fmt.Sprintf("/sys/bus/i2c/devices/%d-00%x/temp1_input", bus, addr)
	raw, err := os.ReadFile(path)
	if err != nil {
		return 0, fmt.Errorf("read %s: %w", path, err)
	}
	millis, err := strconv.Atoi(strings.TrimSpace(string(raw)))
	if err != nil {
		return 0, err
	}
	return float64(millis) / 1000, nil
}
```

```console
$ go test ./...
ok      example.org/sensor    0.012s
```
