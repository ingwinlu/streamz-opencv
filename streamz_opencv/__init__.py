import cv2
from streamz import Source, Stream
from tornado import gen


@Stream.register_api(staticmethod)
class from_opencv(Source):
    """ Stream data from opencv """
    def __init__(self, src, poll_interval=0.01, start=False, **kwargs):
        self.src = src
        self.poll_interval = poll_interval

        super(from_opencv, self).__init__(ensure_io_loop=True, **kwargs)

        self.stopped = True

        if start:
            self.start()

    def start(self):
        if self.stopped:
            self.stopped = False
            self.stream = cv2.VideoCapture(self.src)
            self.loop.add_callback(self.poll_opencv)

    def stop(self):
        if not self.stopped:
            self.stream.release()
            self.stream = None
            self.stopped = True

    def do_poll(self):
        if self.stopped:
            return
        grabbed, frame = self.stream.read()
        if grabbed:
            return frame

    @gen.coroutine
    def poll_opencv(self):
        while not self.stopped:
            frame = self.do_poll()
            if frame is not None:
                yield self._emit(frame)
            else:
                yield gen.sleep(self.poll_interval)
