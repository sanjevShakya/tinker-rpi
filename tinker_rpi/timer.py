import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        """Start a new timer"""
        if self.start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self.start_time = time.perf_counter()

    def get_ellapsed_time(self):
        return time.perf_counter() - self.start_time

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self.start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def restart(self):
        if self.start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        self.start_time = time.perf_counter()
