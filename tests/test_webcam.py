from streamz import Stream
from tornado import gen

from streamz_opencv import from_opencv


def test_from_webcam():
    stream = Stream.from_opencv("0", asynchronous=True)
    out = stream.sink_to_list()
    stream.start()
    yield gen.sleep(0.1)
