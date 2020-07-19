from threading import Thread

import cv2
import numpy as np
from streamz import Source, Stream
from tornado import gen


class WebcamVideoStream(Thread):
    def __init__(self, src=0):
        super().__init__()
        self.stopped = False
        self.stream = cv2.VideoCapture(src)
        self.daemon = True
        self.update()

    def run(self):
        while not self.stopped:
            self.update()

    def read(self):
        return self.grabbed, self.frame

    def update(self):
        self.grabbed, self.frame = self.stream.read()

    def stop(self):
        self.stopped = True


@Stream.register_api(staticmethod)
class from_opencv(Source):
    """ Stream data from opencv """
    def __init__(self, src, poll_interval=0.1, start=False, **kwargs):
        self.src = src
        self.poll_interval = poll_interval

        super(from_opencv, self).__init__(ensure_io_loop=True, **kwargs)

        self.stopped = True

        if start:
            self.start()

    def start(self):
        if self.stopped:
            self.stopped = False
            self.last_frame = None
            self.stream = WebcamVideoStream(self.src)
            self.stream.start()
            self.loop.add_callback(self.poll_opencv)

    def stop(self):
        if not self.stopped:
            self.stream.stop()
            self.stream.join()
            self.stream = None
            self.stopped = True

    def do_poll(self):
        if self.stopped:
            return
        grabbed, frame = self.stream.read()
        if grabbed and np.any(frame != self.last_frame):
            # Check if frames differ to not emit identical images
            self.last_frame = frame
            return frame

    @gen.coroutine
    def poll_opencv(self):
        while not self.stopped:
            frame = self.do_poll()
            if frame is not None:
                yield self._emit(frame)
            else:
                yield gen.sleep(self.poll_interval)
