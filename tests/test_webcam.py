import pytest
from streamz import Stream
from tornado import gen

from streamz_opencv import from_opencv  # NOQA


@pytest.mark.gen_test
def test_from_webcam():
    stream = Stream.from_opencv(0, asynchronous=True)
    out = stream.sink_to_list()
    assert len(out) == 0
    stream.start()
    for _ in range(10):
        yield gen.sleep(0.1)
    
    # Default poll interval is 0.1
    # Should produce at least 10 frames in 1s
    assert len(out) >= 10
    stream.stop()
