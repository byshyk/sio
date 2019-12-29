## SIO
SIO provides shorter and less readable aliases for [ShortIO](https://github.com/byshyk/shortio).



### Installation
```bash
pip install sio
```

### Usage
```python
from sio import *

s = r('filename')
w('filename', s)

j = rjsn('filename.json')
wjsn('filename.json', j)

...
```
