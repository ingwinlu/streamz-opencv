# streamz-opencv

Provide an opencv capture source for [streamz](https://streamz.readthedocs.io/en/latest/).

# Quickstart

Install `streamz` and `streamz-opencv`:
```bash
python -m pip install streamz streamz-opencv
```

Build your pipeline:
```python
import cv2
from streamz import Stream
import streamz_opencv

def scale(img, scale=1.0):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized


def save(img, path):
    cv2.imwrite(path, img)

stream = Stream.from_opencv(0, asynchronous=True)
stream.map(scale, scale=0.5).sink(save, path='small.jpg')
stream.map(scale, scale=1.5).sink(save, path='big.jpg')
stream.start()
```

## good to know
* testing via pytest
* dep management via venv+setup.py+pip-tools
* see example usage in test
