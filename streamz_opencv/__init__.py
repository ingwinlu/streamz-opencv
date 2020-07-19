import cv2
from streamz.core import Source, Stream
from tornado import gen


@Stream.register_api(staticmethod)
class from_opencv(Source):
    """ Stream data from opencv """
    def __init__(self, src: str, poll_interval=0.1, start=False, **kwargs):
        self.src = src
        self.poll_interval = poll_interval

        super(from_opencv, self).__init__(ensure_io_loop=True, **kwargs)

        self.stopped = True
        self.started = False

        if start:
            self.start()

    def start(self):
        if self.stopped:
            self.stopped = False
            self.started = True
            self.stream = cv2.VideoCapture(self.src)
            self.loop.add_callback(self.poll_opencv)

    def do_poll(self):
        grabbed, frame = self.stream.read()
        if grabbed:
            return frame

    @gen.coroutine
    def poll_opencv(self):
        while True:
            frame = self.do_poll()
            if frame:
                yield self._emit(frame)
            else:
                yield gen.sleep(self.poll_interval)
            if self.stopped:
                break
        self.stream.release()
