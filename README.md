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

# Unfortunately pickle -> pckl according to shortening algorithm.
p = rpckl('filename.pickle')
wpckl('filename.pickle', p)

y = ryml('filename.yaml')
wyml('filename.yaml', y)
```
